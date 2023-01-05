import cv2
import numpy as np
from config import BOXES


def find_countours_in_board(crop_image, image_number):
    detected_list = []
    kernel = np.ones((3, 3), np.uint8)
    gray = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
    img_dilation = cv2.dilate(gray, kernel, iterations=1)
    edged = cv2.Canny(img_dilation, 50, 200)
    # cv2.imshow("canny", edged)
    contours, hierarchy = cv2.findContours(edged,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    min_area = 10
    # max_area = 600
    if len(contours) > 5:
        for c in contours:
            area = cv2.contourArea(c)

            # if area > min_area and area < max_area:
            if area > min_area:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.04 * peri, True)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(c)
                    ROI = crop_image[y:y + h, x:x + w]
                    # cv2.waitKey(1)
                    cv2.rectangle(crop_image, (x, y), (x, y), (36, 255, 12), 2)
                    detected_list.append((x, y))

                    image_number += 1

    return image_number, detected_list


faceCascade = cv2.CascadeClassifier('/home/abdullah/Movrs/Movrs Projects/sky_interface/camera_module/cascade.xml')


def find_volume_callibration_board(frame,boxes):
    print("volume")
    flag = False
    faces = faceCascade.detectMultiScale(frame,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(40, 40),
                                         maxSize=(150, 150),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        board_image = frame[y:y + h, x:x + w]
        # flag = True
        image_number = 0

        image_number, detected_list = find_countours_in_board(board_image, image_number)
        if image_number >= 2:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # board_image = frame[y:y + h, x:x + w]
            flag = True
            print("found", boxes)
            # white_rect = np.ones(board_image.shape, dtype=np.uint8) * 255
            # res = cv2.addWeighted(board_image, 0.5, white_rect, 0.5, 1.0)
            # frame[y:y + h, x:x + w] = res

    return flag, frame
