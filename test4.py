from tkinter import *
from tkinter import ttk, font
from PIL import ImageTk, Image
import time
import json
# from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib import animation
from graph_data import GraphData
import os

class ChartWindow:
    def __init__(self, parent):
        # variable intialization
        self.parent = parent
        # Creating a Font object of "TkDefaultFont"
        # self.defaultFont = font.nametofont("TkDefaultFont")
  
        # # Overriding default-font with custom settings
        # # i.e changing font-family, size and weight
        # self.defaultFont.configure(family="Segoe Script",
        #                            size=19,
        #                            weight=font.BOLD)
        self.graph_array = []
        self.x = [0]
        self.y = [0]
        self.recorded_data = []
        self.joints =  []

        self.total_buttons=0
        self.run_first=0
        self.button_row = 0
        self.button_col = 0

        self.f1_style = ttk.Style()
        self.f1_style.configure('My.TFrame', background='#334353')

        self.f1 = ttk.Frame(self.parent, style='My.TFrame')  # added padding
        self.f2 = ttk.Frame(self.f1 )

        self.tabControl = ttk.Notebook(self.f1)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text ='Tab 1')
        self.tabControl.add(self.tab2, text ='Tab 2')

        self.buttons =[]
        self.start_record = 0 

        ttk.Label(self.tab2,text ="Lets dive into theworld of computers").grid(column = 0,row = 0, padx = 30,pady = 30)

        #rows colomn 
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        # col and rows configs
        self.f1.columnconfigure(0, weight=3)
        self.f1.columnconfigure(1, weight=3)
        self.f1.columnconfigure(2, weight=3)
        self.f1.columnconfigure(3, weight=2)
        self.f1.rowconfigure(1, weight=1)
        self.f2.columnconfigure(0, weight=1)
        self.f2.rowconfigure(0, weight=1)
        # grid configs
        self.f1.grid(column=0 , row=0, sticky=(N, S, E, W))  # added sticky
        self.f2.grid(column=0,row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))  # added sticky

        # intialize graph data
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))

        # graph data to plot 
        self.x = [0]
        self.y = []
        # self.y2 = [0]
        # self.y3 = [0]

        # graph data initialize
        self.ln = []
        self.ln2, = plt.plot(self.x, [0], '-')
        # self.ln3, = plt.plot(self.x, self.y, '-')

        # graph axis initialize
        plt.axis([0, 50, 0, 20])

        #initialize object for graph class
        self.obj = GraphData()
        self.obj.start_proces()

        
        self.canvas = FigureCanvasTkAgg(self.fig,self.f2)  
        self.canvas.draw()
        # placing the canvas on the Tkinter window

        self.canvas.get_tk_widget().grid(column=0,row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))  # added sticky
        self.tabControl.grid(column=3, row=0, columnspan=2, sticky=(N, E, W), padx=5,pady=5)  # added sticky, padx

        # animation for graph data to plot 
        self.anim = animation.FuncAnimation(self.fig, self.update_graph,frames=200, interval=20, blit=True)


    # graph data 
    def update_graph (self,frame):
        # take latest data from class object 
        bvh = self.obj.bvh_data.get()
        result = self.obj.result_array.get()
        time_now  = self.obj.time_now.get()
        self.joints  = self.obj.joints_name.get()
        bvh_header = self.obj.bvh_header_data.get()
        # to initalize data on first run
        if self.run_first == 0:
            self.run_first = 1
            # initialize start stop recording button 
            start_recording_btn = ttk.Button(self.tab1, text ="Start Recording ", command = self.start_recording)
            stop_recording_btn = ttk.Button(self.tab1, text ="Stop Recording ", command = self.stop_recording)

            start_recording_btn.grid(pady = 2,row=0,column=0)
            stop_recording_btn.grid(pady = 2,row=0,column=1)

            # all buttons for joints 
            for x in range(0, len(self.joints)):
                # 5 buttons per row
                if( x%5  == 0 ):
                    self.button_row += 1
                    self.button_col = 0

                self.y.append([0])
                self.ln.append(plt.plot(self.x,[0], '-'))   


                self.buttons.append(ttk.Button(self.tab1, text=self.joints[x], command =lambda num = x : self.button_click(num)))
                self.buttons[x].grid(pady = 2,row=self.button_row,column=self.button_col)
                self.total_buttons = x
                self.button_col += 1
                # initalize data record array with bvh header 
                self.recorded_data = []
                self.recorded_data.append( 
                    {   
                        "bvh_header":bvh_header,
                    }
                )

        # when record data press it will start saving data in to a variable 
        if (self.start_record == 1 ):
            self.recorded_data.append( 
                {   
                    "bvh": bvh,
                    "joints" :self.joints ,
                    "result": result,
                    "time_now": time_now
                }
            )
        result_array = []
        #append data to show on graph
        if(len(self.graph_array)>0):
            
            self.x.append(time_now)
            for count in range(0, len(self.joints)):
                self.y[count].append(result[count])
                self.ln[count][0].set_data(self.x, self.y[count]) 
                # result_array.append(self.ln[count][0])

            for c in range(0, len(self.graph_array)):
                result_array.append(self.ln[self.graph_array[c]][0])
            return result_array
        else:
            return [self.ln2]

    def button_click(self,index):
        self.graph_array.append(index)

        

    # for recording button function
    def start_recording(self):
        self.start_record = 1 
    # for stop recording function
    def stop_recording(self):
        self.start_record = 0 
        # save recorded data to json file in storage folder with current time stamp 
        with open("storage/"+str(time.time())+".json", "w") as outfile:
            json.dump(self.recorded_data, outfile)
        # this will clean all the data in recorded data 
        self.recorded_data= []
        self.recorded_data.append( 
            {   
                "bvh_header":"Bvh header ",
            }
        )