import cv2
from multiprocessing import Process, Queue

import random

class StreamVideos:
    def __init__(self):
        self.image_data = Queue()

    def start_proces(self):
        p = Process(target=self.echo)
        p.start()

    def echo(self):
        cap = cv2.VideoCapture('videoplayback.mp4')
        while cap.isOpened():
            ret,frame = cap.read()
            if ret:
                self.image_data.put(random.randint(0,9))

