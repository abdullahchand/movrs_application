import EasyPySpin
from camera_module.volume_callibration import find_volume_callibration_board
from camera_module.file_handling import write_file, delete_file
from camera_module.frame_queue import FrameQueue
from camera_module.record_video import lens_calibration, volume_recording
from config import CTI_FILE

from threading import Thread
from multiprocessing import Process,Queue

import cv2
import time
from concurrent.futures import ThreadPoolExecutor


class GigeVisionStreamReader:

    def __init__(self):
        self.live_frame = []
        self.WIDTH = 720  # Image buffer width as per the camera output
        self.HEIGHT = 540  # Image buffer height as per the camera output
        self.PIXEL_FORMAT = "BayerRG8"  # Camera pixel format as per the camera output
        self.FPS = None
        self.FRAME_QUEUE = []
        self.cap = []
        self.THREAD_FLAG = []
        # self.h.add_file("C:\\Program Files\\MATRIX VISION\\mvIMPACT Acquire\\bin\\x64\\mvGenTLProducer.cti") # Add path to mvGenTLProducer.cti
        # self.h.add_file("/opt/mvIMPACT_Acquire/lib/x86_64/mvGenTLProducer.cti") # Add path to mvGenTLProducer.cti
        # self.h.add_file(CTI_FILE)

        # self.h.add_file("C:\\Program Files\\MATRIX VISION\\mvIMPACT Acquire\\bin\\x64\\mvGenTLProducer.cti") # Add path to mvGenTLProducer.cti
        # self.h.update()
        self.image_acquirer = []
        self.video_writer_stream = []
        self.queue_arr = []
        self.queue_arr2 = []
        self.calibratin_lens_value_queue = []
        self.calibratin_volume_value_queue = []
        self.record = False
        self.stop_record = False
        self.folder_name = ""
        self.volume_callibration_detected = []
        self.volume_callibration_value = []
        self.lens_callibration_value = []
        self.lens_callibration_coverage = []
        self.lens_callibration = False
        self.volume_callibration = False
        self.calibratin = []
        self.noc = 0
        self.cap = []
        self.start_reading = Queue()
        self.trigger = 0
        self.lens_counter = 0
        self.volume_counter_arr = []
        self.BOXES = 7
        # self.is_stop = False
        # print(self.h.device_info_list)


    def start_camera(self):
        for i in range(self.noc):
            p = Process(target=self.get_frames_with_specified_cam,args=(i,))
            p.start()
        
        self.start_reading.put("start")


    def init_cameras(self):
        # self.ps.add(ParameterKey.LOGGER, 1)
        self.noc = 0
        eoc = True
        temp = []
        while eoc:
            cap =  EasyPySpin.VideoCapture(self.noc)
            eoc = cap.get_pyspin_value("DeviceModelName")
            if eoc:
                if not self.FPS:
                    self.FPS = 20
                    if cap.get(cv2.CAP_PROP_FPS) > 30 and cap.get(cv2.CAP_PROP_FPS) <= 60:
                        self.FPS = 30
                    elif cap.get(cv2.CAP_PROP_FPS) > 60:
                        self.FPS = 60
                    print("FPS",self.FPS)
                    print("FPS",cap.get(cv2.CAP_PROP_FPS), self.FPS)
                cap.set(cv2.CAP_PROP_FPS,20)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
                cap.set_pyspin_value("PixelFormat", self.PIXEL_FORMAT)
                self.cap.append(cap)
                self.noc+=1
                self.volume_callibration_detected.append(False)
                self.volume_callibration_value.append(0)
                self.lens_callibration_value.append([])
                self.lens_callibration_coverage.append(0)
                # self.image_acquirer.append(io)
                # self.image_acquirer[i].start()
                self.calibratin.append(True)

                self.queue_arr.append(FrameQueue())
                self.queue_arr2.append(FrameQueue())
                self.calibratin_lens_value_queue.append(FrameQueue())
                self.calibratin_volume_value_queue.append(FrameQueue())
                self.FRAME_QUEUE.append(Queue())
                self.THREAD_FLAG.append(False)
                self.volume_counter_arr.append(0)
        
        # self.trigger = (self.FPS/10)+1
        self.trigger = 1

    def clear_lens_calibration(self):
        for i in range(len(self.lens_callibration_value)):
            self.lens_callibration_value[i] = []
            self.lens_callibration_coverage[i] = 0
        delete_file()
        return 0

    def clear_volume_calibration(self):
        for i in range(len(self.volume_callibration_value)):
            self.volume_callibration_value[i] = 0
        delete_file()
        return 0

    def get_calibration_values(self):
        # print("Calibrating " , self.volume_callibration_value)
        return self.volume_callibration_value

    def start_recording(self, folder_name):
        self.folder_name = folder_name
        for i in range(self.noc):
            # self.queue_arr.append(FrameQueue())
            # process1 =  Thread(target=camera_recording,args=(self.queue_arr[i],))
            # process1.start()
            # print("Here2")
            output_filename = 'storage/' + folder_name + '/stream0' + str(i) + '.avi'  # Save stream
            fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
            out = cv2.VideoWriter(output_filename, fourcc, self.FPS, (self.WIDTH, self.HEIGHT))
            self.video_writer_stream.append(out)
            print("start camera: ", i, "at ", time.time())
        self.record = True

    def stop_recording(self):
        for i in range(self.noc):
            # print(self.queue_arr[i])
            # self.image_acquirer[i].stop_acquisition()
            # self.image_acquirer[i].destroy()
            self.video_writer_stream[i].release()
            print("stop camera: ", i, " at ", time.time())
            # self.is_stop = True         
        self.record = False
        self.video_writer_stream = []


    # def start_threads(self):
    #     executor = ThreadPoolExecutor(self.noc)
    #     for i in range(self.noc):
    #         if not self.THREAD_FLAG[i]:
    #             future = executor.submit(self.get_frames_with_specified_cam, (i))
    #             print("Process Started + " , str(i))
    #     self.start_reading = True

    def get_gige_vision_frames(self):
        # self.live_frame = []
        # frames = []
        # start = time.time()
        while True:
            start = time.time()
            # print("here")
            for i in range(self.noc):
                read_values = self.cap.read()
                # print("Time taken for camera : "  , time.time() - start)
                for i, (ret, frame) in enumerate(read_values):
                    self.FRAME_QUEUE[i].put(frame)

            #     Buffer = self.image_acquirer[i].fetch_buffer(timeout=-1)
            #     component = Buffer.payload.components[0]
            #     # if component.width == 720:
            #     original = component.data.reshape(540, 720)
            #     img = original.copy()
            #     Buffer.queue()
            #     frames.append(img)
            # # print(frames)
            # # print("Time Taken for cam : " , time.time()-start)
            # return frames


    def get_frames_with_specified_cam(self, cam_number):
        flag_start = False
        while True:
            # print("In While Reading Frame for cam : " , str(cam_number))
            if not self.start_reading.empty():
                flag_start = True
            if flag_start:
                # print("Before Reading Frame for cam : " , str(cam_number))
                _ , frame = self.cap[cam_number].read()
                # print("Reading Frame for cam : " , str(cam_number))
                self.FRAME_QUEUE[cam_number].put(frame)
