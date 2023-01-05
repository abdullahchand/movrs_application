import cv2
from multiprocessing import Process, Queue

import random
import time

class StreamVideos:
    def __init__(self):
        self.image_data = Queue()

    def start_proces(self):
        p = Process(target=self.echo)
        p.start()

    def echo(self):
        time.sleep(5)
        cap = cv2.VideoCapture('test.avi')
        while cap.isOpened():
            ret,frame = cap.read()
            self.image_data.put(frame)
