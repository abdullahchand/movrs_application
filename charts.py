# packages
from tkinter import *
from tkinter import ttk, font
import tkinter
from PIL import ImageTk, Image
import time
import json
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib import animation
from graph_data import GraphData


class ChartWindow:
    def __init__(self, parent):
        # variable intialization
        self.parent = parent
        # Creating a Font object of "TkDefaultFont"
        self.graph_array = ['','','']
        self.color_array = ['blue','red','green']
        self.recording_name=tkinter.StringVar()
        self.x = [0]
        self.y = [0]
        self.recorded_data = []
        self.joints =  []
        self.max_y=1
        self.min_y=0
        self.max_x=5
        self.min_x=0   
        self.last_x = 0
        self.total_buttons=0
        self.run_first=0
        self.button_row = 1
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

        Label(self.tab2,text ="Lets dive into theworld of computers").grid(column = 0,row = 0, padx = 30,pady = 30)

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
        
        # graph data to plot 
        self.x = [[],[],[]]
        self.y = [[],[],[]]
        self.tk = None

        # graph data initialize
        self.ln= [[plt.plot([], [], '-', color="blue")],[plt.plot([], [], '-', color="red")],[plt.plot([], [], '-', color="green")]]
        # graph axis initialize
        plt.axis([self.min_x, self.max_x, self.min_y, self.max_y])

        #initialize object for graph class
        self.obj = GraphData()
        self.obj.start_proces()
        self.canvas = FigureCanvasTkAgg(self.fig,self.f2)  
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=True)
        # navigation toolbar
        toolbarFrame = Frame(master=self.tab1)
        toolbarFrame.grid(row=10,columnspan=5, column=0)
        toolbar = NavigationToolbar2Tk( self.canvas,toolbarFrame)
        toolbar.update()
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
            self.lbl = Label(self.tab1, text = "")
            self.start_recording_btn = Button(self.tab1, text ="Start Recording ",bg="green", fg="white", command = self.start_recording)
            self.stop_recording_btn = Button(self.tab1, text ="Stop Recording ",bg="red", fg="white", command = self.stop_recording)

            self.start_recording_btn.grid(pady = 2,row=1,column=0)
            self.stop_recording_btn.grid(pady = 2,row=1,column=1)
            self.lbl.grid(pady = 2,row=0,column=0, columnspan=3)
            # creating a label for password
            passw_label = Label(self.tab1, text = 'Recording name', font = ('calibre',10,'bold'))
            
            # creating a entry for password
            passw_entry=Entry(self.tab1, textvariable = self.recording_name, font = ('calibre',10,'normal'))

            passw_label.grid(row=1,column=2)
            passw_entry.grid(row=1,column=3)
            # all buttons for joints 
            for x in range(0, len(self.joints)):
                # 5 buttons per row
                if( x%5  == 0 ):
                    self.button_row += 1
                    self.button_col = 0
                
                self.buttons.append(Button(self.tab1,bg='white', text=self.joints[x],command =lambda num = x : self.button_click(num)))
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
        # make graph x and y axis dynamically 
        for count in range(0, len(self.graph_array)):
            if(self.graph_array[count] != ""):
                self.y[count].append(result[self.graph_array[count]])
                self.x[count].append(time_now)
                self.ln[count][0][0].set_data(self.x[count], self.y[count]) 
                result_array.append(self.ln[count][0][0])
                if(self.max_y < result[self.graph_array[count]]):
                    self.max_y = result[self.graph_array[count]]
                    plt.axis([self.min_x, self.max_x, self.min_y, self.max_y])
                if( self.max_x < time_now):
                    self.min_x = self.max_x
                    self.max_x =  self.max_x +5
                    plt.axis([self.min_x, self.max_x, self.min_y, self.max_y])
        return result_array



    # this funtion will plot a line on graph 
    def button_click(self,index):
        if(index in self.graph_array):
            self.buttons[index].config(bg='white', fg="black")
            array_index = self.graph_array.index(index)   
            self.graph_array[array_index] = ""
            self.y[array_index]=[]
            self.x[array_index]=[]
            self.displayError("")
        else:
            if( "" in self.graph_array):
                for count in range(0, len(self.graph_array)):
                    if(self.graph_array[count]==""):
                        self.graph_array[count] = index
                        self.buttons[index].config(bg=self.color_array[count], fg="white")
                        break
            else:
                self.displayError("Warning : Please select only 3 joints")


    # Display error messages if user do something wrong 
    def displayError(self,error_text):
        if(error_text!=""):
            self.lbl.config(text = error_text ,bg="red" ,fg="white")
        else:
            self.lbl.config(text = error_text ,bg="#d9d9d9" ,fg="white")

    # for recording button function
    def start_recording(self):
        inp = self.recording_name.get()
        if(inp==""):
            self.displayError("Warning : Please set name of recording")
        else:
            if self.start_recording_btn["state"] == "active":
                self.start_recording_btn["state"] = "disabled"

            self.displayError("")
            self.start_record = 1 

    # for stop recording function
    def stop_recording(self):
        self.start_record = 0 
        inp = self.recording_name.get()
        self.start_recording_btn["state"] = "active"

        # save recorded data to json file in storage folder with current time stamp 
        with open("storage/"+inp+"-"+str(time.time())+".json", "w") as outfile:
            json.dump(self.recorded_data, outfile)
        # this will clean all the data in recorded data 
        self.recorded_data= []
        self.recorded_data.append( 
            {   
                "bvh_header":"Bvh header ",
            }
        )