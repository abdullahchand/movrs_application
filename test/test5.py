
from multiprocessing import Process, Queue
from play_videos import StreamVideos
import multiprocessing


obj = StreamVideos()
# def start_process():


def stream_videos():
    count= 0
    while True:
        # print("working")
        try:
            img = obj.get_frame()
            print(img)
            print("getframe =", count)
            count +=1
        except:
            break
        # .img = Image.open("1.jpg")
        # print(img)

        # self.resized_img = self.img.resize((self.main_video.winfo_width(),self.main_video.winfo_height()))
        # print("working3")
        
        # self.new_bg = ImageTk.PhotoImage(self.resized_img )
        # print("working4")
        
        # self.canvas.create_image(0.5,0.5,anchor=NW,image=self.img)
if __name__ == '__main__':
    stream_videos()