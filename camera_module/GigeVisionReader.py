# Import Libraries
# from numpy import *
# import time
import cv2
from harvesters.core import Buffer, Harvester

# Set width, height and pixel format of frame if you know the details.
WIDTH = 720  # Image buffer width as per the camera output
HEIGHT = 540  # Image buffer height as per the camera output
PIXEL_FORMAT = "BGR8"  # Camera pixel format as per the camera output


def get_gige_vision_frames():
    h = Harvester()
    h.add_file(
        "/opt/mvIMPACT_Acquire/lib/x86_64/mvGenTLProducer.cti") # Add path to mvGenTLProducer.cti
    # h.files
    h.update()
    print(h.device_info_list)
    # while True:
    # dic = {}
    frames = []
    for i in range(len(h.device_info_list)):
        print(i)
        io = h.create_image_acquirer(i)
        io.remote_device.node_map.Width.value = WIDTH
        io.remote_device.node_map.Width.value = WIDTH
        io.remote_device.node_map.PixelFormat.value = PIXEL_FORMAT
        # io.remote_device.node_map.AcquisitionFrameRate.value = fps # Set if required
        io.start_acquisition()

        frame = []
        i = 0
        Buffer = io.fetch_buffer(timeout=-1)
        component = Buffer.payload.components[0]
        # print(component.width)
        if component.width == 720:  # To make sure the correct size frames are passed for converting
            original = component.data.reshape(540, 720, 3)
            img = original.copy()  # To prevent isues due to buffer queue

            # cv2.imshow("cam"+str(i), img)
            frame = img
            # cv2.waitKey(1)
                # cv2.imwrite('img.png', img)
                # out.write(cv2.resize(img, (720, 540, 3)))
            Buffer.queue()
                # time.sleep(0.03)
            i += 1
        else:
            i += 1
        # dic[i] = frame
        frames.append(frame)
        io.stop_acquisition()
        io.destroy()
            # h.reset()
            # cv2.destroyAllWindows()

    # return dic
    print(frames)
    return frames 



print(get_gige_vision_frames())