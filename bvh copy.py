#
# Laying out a tkinter grid
#
# Please also find two images:
#    GridLayout.png and screenshot.png
# Credit: Modified by Larz60+ From the original:
#    'http://www.tkdocs.com/tutorial/grid.html'
#    
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
import os, sys, subprocess
from charts import ChartWindow
from play_videos import StreamVideos
from multiprocessing import Process, Queue
import threading
import cv2
# from tkinterweb import HtmlFrame
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
class BVHWindow:
    def __init__(self, parent):
        # root = parent 
        self.parent = parent

        self.number_of_cameras = 8
        self.buttons =[]
        #initialize object for graph class

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



        # self.img = ImageTk.PhotoImage(Image.open("black.jpg"))
        # self.canvas= Canvas( self.main_video)
        # self.canvas.create_image(0.5,0.5,anchor=NW,image=self.img)
        # self.canvas.grid(column=0 ,row =0 ,sticky="NSEW")
        # self.button_col=0

        self.main_video.columnconfigure(0, weight=1)
        self.main_video.rowconfigure(0, weight=1)

        self.bottom_video_list.columnconfigure(0, weight=1)
        self.bottom_video_list.rowconfigure(0, weight=1)

        self.main_window.grid(column=0 , row=0, sticky=(N, S, E, W))  # added sticky
        self.main_video.grid(column=0,row=0, columnspan=3, rowspan=3, sticky=(N, S, E, W))  # added sticky



    def resizeApp(self,e):

        start = time.time()
        self.img = Image.open("black.jpg")
        self.resized_img = self.img.resize((self.main_video.winfo_width(),self.main_video.winfo_height()))
        self.new_bg = ImageTk.PhotoImage(self.resized_img )
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.new_bg)
