import cv2
from multiprocessing import Process, Queue


class StreamVideos:
    def __init__(self):
        self.image_data = Queue()
        self.cap = cv2.VideoCapture('basic_animation.mp4')

    def start_proces(self):
        p = Process(target=self.echo)
        p.start()

    def echo(self):
        cap = cv2.VideoCapture('videoplayback.mp4')
        count= 0
        while cap.isOpened():
            ret,frame = cap.read()
            self.image_data.put(frame)
            print("putframe =", count)
            count +=1
            # print("frame")
    
    def get_frame(self):
        if self.cap.isOpened():
            ret,frame = self.cap.read()
            return frame
        else:
            return None

         