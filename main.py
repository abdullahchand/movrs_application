from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
import os, sys, subprocess
from charts import ChartWindow
import subprocess   
from play_videos import StreamVideos
from multiprocessing import Process, Queue
import threading
import cv2
from tkinter import messagebox


class ResizableWindow:
    def __init__(self, parent):
        # root = parent 
        self.parent = parent

        self.number_of_cameras = 8
        self.sample_cams_width = 100
        self.buttons =[]
        #initialize object for graph class
        self.obj = StreamVideos()
        self.parent.title("Movrs Application")
        #creating menu_bar for top 
        self.menubar = Menu(self.parent )  
        self.file = Menu(self.menubar, tearoff=0)  
 
        self.menubar.add_cascade(label="Charts",command = self.openCharts)  
        self.menubar.add_cascade(label="BVH",command = self.openBVH)  
        self.parent.config(menu=self.menubar)  

        #main window 
        self.main_window_style = ttk.Style()
        self.main_window_style.configure('My.TFrame', background='#334353')
        self.main_window = ttk.Frame(self.parent, style='My.TFrame' )  # added padding

        #root or parent weight for column
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        
        #main_window weight for column (0,1,2) cols for main video (3) for right tab boxes 
        self.main_window.columnconfigure(0, weight=3)
        self.main_window.columnconfigure(1, weight=3)
        self.main_window.columnconfigure(2, weight=3)
        self.main_window.columnconfigure(3, weight=4)

        #main_window weight for rows (1) col for bottom row 
        self.main_window.rowconfigure(1, weight=2)

        # main_video frame for main video
        self.main_video = ttk.Frame(self.main_window )

        # display other cameras images in given child tab 
        self.bottom_frames = ttk.Frame(self.main_window )

        # bottom_video_list is a child of bottom_frames
        self.bottom_video_list = ttk.Frame(self.bottom_frames)

        # right box 1 
        self.right_box_1 = ttk.Notebook(self.main_window)
        self.right_box_tab_1 = ttk.Frame(self.right_box_1)
        self.right_box_tab_2 = ttk.Frame(self.right_box_1)
        self.right_box_1.add(self.right_box_tab_1, text ='Tab 1')
        self.right_box_1.add(self.right_box_tab_2, text ='Tab 2')

        ttk.Label(self.right_box_tab_1, text ="right_box_1").grid(column = 0,row = 0,padx = 30,pady = 30)  
        ttk.Label(self.right_box_tab_2, text ="Lets dive into the\world of computers").grid(column = 0,row = 0, padx = 30,pady = 30)
        self.right_box_1.grid(column=3, row=0, columnspan=2, sticky=(N, E, W, S), padx=5,pady=5)  


        # right box 1    
        self.right_box_2 = ttk.Notebook(self.main_window)
        self.right_box_2_tab_1 = ttk.Frame(self.right_box_2)
        self.right_box_2_tab_2 = ttk.Frame(self.right_box_2)
        self.right_box_2.add(self.right_box_2_tab_1, text ='Tab 1')
        self.right_box_2.add(self.right_box_2_tab_2, text ='Tab 2')

        ttk.Label(self.right_box_2_tab_1, text ="right_box 2").grid(column = 0,row = 0,padx = 30,pady = 30)  
        ttk.Label(self.right_box_2_tab_2,text ="Lets dive into theworld of computers").grid(column = 0,row = 0, padx = 30,pady = 30)
        self.right_box_2.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), padx=5,pady=5)  # added sticky, padx


        # Video box 1  
        self.bottom_tab_box = ttk.Notebook(self.bottom_video_list)
        self.bottom_tab_1 = ttk.Frame(self.bottom_tab_box)
        self.bottom_tab_2 = ttk.Frame(self.bottom_tab_box)
        self.bottom_tab_box.add(self.bottom_tab_1, text ='Live View')
        self.bottom_tab_box.add(self.bottom_tab_2, text ='Preview')
        
        self.bottom_tab_box.grid(column=0, row=0, columnspan=4, sticky=(N, E, W, S), padx=5,pady=5)  # added sticky, padx

        self.img = ImageTk.PhotoImage(Image.open("images/black.jpg"))
        self.canvas= Canvas( self.main_video)
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas.grid(column=0 ,row =0 ,sticky="NSEW")
        self.button_col=0
        self.img2 = Image.open("images/black.jpg")
        self.resized_img2 = self.img2.resize((100,100))
        self.new_bg2 = ImageTk.PhotoImage(self.resized_img2 )

        for x in range(0, self.number_of_cameras):
            self.buttons.append(Button(self.bottom_tab_1,bg='white', text='button',image = self.new_bg2))
            self.buttons[x].grid(pady = 2,row=0,column=self.button_col)
            self.total_buttons = x
            self.button_col += 1
 

        # setup row and cols for all frames 
        self.main_video.columnconfigure(0, weight=1)
        self.main_video.rowconfigure(0, weight=1)

        self.bottom_tab_1.rowconfigure(0, weight=1)

        self.bottom_video_list.columnconfigure(0, weight=1)
        self.bottom_video_list.rowconfigure(0, weight=1)

        self.main_window.grid(column=0 , row=0, sticky=(N, S, E, W))  # added sticky
        self.main_video.grid(column=0,row=0, columnspan=3, rowspan=3, sticky=(N, S, E, W))  # added sticky

        self.bottom_frames.grid(column=0,row=3, columnspan=5, rowspan=1, sticky=(N, S, E, W))  # Bottom

        self.bottom_video_list.grid(column=0,row=0, columnspan=5, rowspan=1, sticky=(N, S, E, W))  # Bottom
        
        self.bottom_frames.columnconfigure(1, weight=3)
        self.bottom_frames.columnconfigure(2, weight=3)
        self.bottom_frames.columnconfigure(3, weight=3)
        self.bottom_frames.columnconfigure(4, weight=3)

        self.start_process()

    # function that charts /graphs bvh file
    def openCharts(self):
        self.top= Toplevel(self.parent)
        self.top.geometry("750x250")
        self.top.title("Charts")
        cw = ChartWindow(self.top)

    # function that open bvh file
    def openBVH(self):
        subprocess.Popen('python bvh.py', shell=True)

    # function for resize app widgets
    def resizeApp(self,e):
        start = time.time()
        self.img = Image.open("images/black.jpg")
        self.resized_img = self.img.resize((self.main_video.winfo_width(),self.main_video.winfo_height()))
        self.new_bg = ImageTk.PhotoImage(self.resized_img )
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.new_bg)


    def start_process(self):
        # calling StreamVideos function start_process()
        self.obj.start_proces()

        # create a thread and run video stream on it 
        t2 = threading.Thread(target=self.stream_videos)
        t2.start()
        


    def stream_videos(self):
        while True:
            self.img = self.obj.image_data.get()
            blue,green,red = cv2.split(self.img)
            img = cv2.merge((red,green,blue))
            im = Image.fromarray(img)
            # resize the pictures to fit in dynamically
            self.resized_img = im.resize((self.main_video.winfo_width(),self.main_video.winfo_height()))
            if((self.parent.winfo_width()/8) < 107):
                self.sample_cams_width = int((self.parent.winfo_width()/8)- 6)
            else:
                self.sample_cams_width = 100
            self.resized_img2 = im.resize((self.sample_cams_width,self.sample_cams_width))

            self.new_bg = ImageTk.PhotoImage(image=self.resized_img)
            self.canvas.create_image(0.5,0.5,anchor=NW,image=self.new_bg)
            self.new_bg2 = ImageTk.PhotoImage(self.resized_img2 )
            # 8 camera buttons 
            self.buttons[0]['image'] = self.new_bg2
            self.buttons[1]['image'] = self.new_bg2
            self.buttons[2]['image'] = self.new_bg2
            self.buttons[3]['image'] = self.new_bg2
            self.buttons[4]['image'] = self.new_bg2
            self.buttons[5]['image'] = self.new_bg2
            self.buttons[6]['image'] = self.new_bg2
            self.buttons[7]['image'] = self.new_bg2

    # on close text
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.parent.destroy()

       



def main():
    root = Tk()
    rw = ResizableWindow(root)

    # open in full windoww for linux and windows
    # root.wm_state('zoomed')
    # root.attributes('-zoomed', True)

    root.bind('<Configure>',rw.resizeApp)


    root.protocol("WM_DELETE_WINDOW", rw.on_closing) 

    root.mainloop()
 
 
if __name__ == '__main__':
    main()