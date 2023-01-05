from camera_module.lens_callibration import find_board
from camera_module.volume_callibration import find_volume_callibration_board
import cv2
import numpy as np

def overlay_func(frame,dets,overlay = None,ret = False):
    # loop over the alpha transparency values
    for alpha in np.arange(0, 1.1, 0.1)[::-1]:
        # create two copies of the original image -- one for
        # the overlay and one for the final output image
        if ret == False:
            overlay = frame.copy()
        # draw a red rectangle surrounding Adrian in the image
        # along with the text "PyImageSearch" at the top-left
        # corner

        # for cord in dets:
        try:
            print("points : ", dets)
            # for points in dets[1]:
                # cv2.rectangle(overlay, (dets[0][0] + points[0], dets[0][1] + points[1]),
                #             (dets[0][0] + points[0], dets[0][1] + points[1]), (36, 255, 12), 2)
        except Exception as e:
            print("exception : , " , e)
            return False , None
        return True, overlay[:, :, 3]

def lens_calibration(queue_frame, lens_value_queue,Boxes):
    mask = None
    # while True:
    if not queue_frame.queue.empty():
        frame  = queue_frame.queue.get()
        print("Before find board")
        detection = find_board(frame,Boxes)
        # ret,ov = overlay_func(frame,detection,mask,ret=False)

        # print("After overlay")
        # if ret ==  True:
        #     mask = ov
        lens_value_queue.queue.put(detection)


def volume_calibration(queue_frame,boxes):
    if not queue_frame.queue.empty():
        frame  = queue_frame.queue.get()
        # print("Before find board")
        flag, frame  = find_volume_callibration_board(frame,boxes)

    return flag, frame

def volume_recording(queue_frame, volume_value_queue):
    while not queue_frame.queue.empty():
        flag, frame = find_volume_callibration_board(queue_frame.queue.get())
        volume_value_queue.queue.put(flag)
