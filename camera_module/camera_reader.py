from imutils.video import FileVideoStream as Fvs
import cv2

class StreamReader:

    def __init__(self, data_path,num_cameras,data_type="video") -> None:
        self.data_path = data_path
        self.num_cameras = num_cameras
        self.streamer = []
        self.data_type = data_type
    def start_camera(self):
        for i in range(0,self.num_cameras+1):
            if self.data_type == "video":
                self.streamer.append(Fvs(path=self.data_path+str(i)+".avi"))
            self.streamer[i].start()
    
    def get_frame(self):
        frames = []
        for i in range(0,self.num_cameras+1):
            image = self.streamer[i].read()
            image= cv2.resize(image, (300,300))
            frames.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return frames
    
    def stop_camera(self):
        for i in range(0,self.num_cameras+1):
            self.streamer[i].stop()