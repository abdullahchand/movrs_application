import cv2
import numpy as np
from config import CASCADE_FILE
from camera_module.file_handling import write_file

List_found = []


def find_countours_in_board(crop_image, image_number):
    detected_list = []
    kernel = np.ones((3, 3), np.uint8)
    gray = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
    img_dilation = cv2.dilate(gray, kernel, iterations=1)
    edged = cv2.Canny(img_dilation, 50, 200)
    # cv2.imshow("canny", edged)
    contours, hierarchy = cv2.findContours(edged,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    min_area = 100
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
                    # cv2.imshow("board", crop_image)

    return image_number, detected_list


faceCascade = cv2.CascadeClassifier(CASCADE_FILE)
# faceCascade = cv2.CascadeClassifier('/home/abdullah/Movrs/Movrs Projects/sky_interface/camera_module/cascade.xml')
# video_capture = cv2.VideoCapture('/home/abdullah/Movrs/Movrs Projects/sky_interface/camera_module/stream01.avi')
# list_of_detected_points = []

def find_board(frame,boxes):
    print("lens")
    detection = []

# while True:
    # ret, frame = video_capture.read()
    faces = faceCascade.detectMultiScale(frame,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(200, 200),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        board_image = frame[y + 10:y + h - 10, x + 80:x + w - 80]
        image_number = 0
        image_number, detected_list = find_countours_in_board(board_image, image_number)
        if image_number >= 7:
            # list_of_detected_points.append([(x+80, y+10), detected_list])
            # gige_vision_streamer.lens_callibration_value[cam_number].append([(x+80, y+10), detected_list])
            # lens_value_queue.queue.put([(x+80, y+10), detected_list])
            detection = [(x+80, y+10), detected_list]
            print("found", boxes)
            # gige_vision_streamer.lens_callibration_coverage[cam_number] += 1
            # data = {"type":"lens_callibration","value":gige_vision_streamer.lens_callibration_coverage, "cam_no" :cam_number}
            # write_file(data)
            # white_rect = np.ones(board_image.shape, dtype=np.uint8) * 255
            # res = cv2.addWeighted(board_image, 0.5, white_rect, 0.5, 1.0)
            # frame[y + 10:y + h - 10, x + 80:x + w - 80] = res

    # for cord in gige_vision_streamer.lens_callibration_value[cam_number]:
    #     for points in cord[1]:
    #         cv2.rectangle(frame, (cord[0][0] + points[0], cord[0][1] + points[1]),
    #                     (cord[0][0] + points[0], cord[0][1] + points[1]), (36, 255, 12), 2)

    # cv2.imshow('Video', frame)

    # cv2.waitKey(500)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
# video_capture.release()
# cv2.destroyAllWindows()

    return detection