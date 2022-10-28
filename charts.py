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
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
class ResizableWindow:
    def __init__(self, parent):
        self.parent = parent
        self.f1_style = ttk.Style()

        self.f1_style.configure('My.TFrame', background='#334353')

        self.f1 = ttk.Frame(self.parent, style='My.TFrame')  # added padding

        self.f2 = ttk.Frame(self.f1 )
        self.tabControl = ttk.Notebook(self.f1)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.tab1, text ='Tab 1')
        self.tabControl.add(self.tab2, text ='Tab 2')
        # self.tabControl.pack(expand = 1, fill ="both")

        # ttk.Label(self.tab1, 
        #   text ="Welcome to \
        #   GeeksForGeeks").grid(column = 0, 
        #                        row = 0,
        #                        padx = 30,
        #                        pady = 30)  
        
        button1=ttk.Button(self.tab1, text="button1")
        button1.grid(pady = 2,row=0,column=0)

        button2=ttk.Button(self.tab1, text="button2")
        button2.grid(pady = 2,row=0,column=1)

        button3=ttk.Button(self.tab1, text="button3")
        button3.grid(pady = 2,row=0,column=2)

        button4=ttk.Button(self.tab1, text="button4")
        button4.grid(pady = 2,row=0,column=3)

        button5=ttk.Button(self.tab1, text="button5")
        button5.grid(pady = 2,row=0,column=4)

        button6=ttk.Button(self.tab1, text="button1")
        button6.grid(pady = 2,row=1,column=0)

        button7=ttk.Button(self.tab1, text="button2")
        button7.grid(pady = 2,row=1,column=1)

        button8=ttk.Button(self.tab1, text="button3")
        button8.grid(pady = 2,row=1,column=2)

        button9=ttk.Button(self.tab1, text="button4")
        button9.grid(pady = 2,row=1,column=3)

        button10=ttk.Button(self.tab1, text="button5")
        button10.grid(pady = 2,row=1,column=4)
        ttk.Label(self.tab2,
                text ="Lets dive into the\
                world of computers").grid(column = 0,
                                            row = 0, 
                                            padx = 30,
                                            pady = 30)

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.f1.columnconfigure(0, weight=3)
        self.f1.columnconfigure(1, weight=3)
        self.f1.columnconfigure(2, weight=3)
        self.f1.columnconfigure(3, weight=2)
        # self.f1.columnconfigure(4, weight=2)
        self.f1.rowconfigure(1, weight=1)
        self.f2.columnconfigure(0, weight=1)
        self.f2.rowconfigure(0, weight=1)
  
  
        # self.one = ttk.Checkbutton(self.f1, text="One",  onvalue=True)
        # self.two = ttk.Checkbutton(self.f1, text="Two",  onvalue=True)
        # self.three = ttk.Checkbutton(self.f1, text="Three",  onvalue=True)
        # self.ok = ttk.Button(self.f1, text="Okay")
        # self.cancel = ttk.Button(self.f1, text="Cancel")
       

        self.f1.grid(column=0 , row=0, sticky=(N, S, E, W))  # added sticky
        self.canvas= Canvas( self.f2)
        self.f2.grid(column=0,row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))  # added sticky

        self.canvas.grid(column=0 ,row =0 ,sticky="NSEW")

        self.fig = Figure(figsize = (5, 5),
                    dpi = 100)
    
        # list of squares
        self.y = [i**2 for i in range(101)]
    
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
    
        # plotting the graph
        self.plot1.plot(self.y)
    
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig,self.f2)  
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        
        self.canvas.get_tk_widget().grid(column=0,row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))  # added sticky

        self.tabControl.grid(column=3, row=0, columnspan=2, sticky=(N, E, W), padx=5,pady=5)  # added sticky, padx
        # self.label.grid(column=0 ,row =0 ,sticky="NSEW")
        # Create an object of tkinter ImageTk

    
        # # creating the Matplotlib toolbar
        # toolbar = NavigationToolbar2Tk(self.canvas,
        #                             window)
        # toolbar.update()

        # self.name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)  # added sticky, pady, padx
        # self.one.grid(column=0, row=3)
        # self.two.grid(column=1, row=3)
        # self.three.grid(column=2, row=3)
        # self.ok.grid(column=3, row=3)
        # self.cancel.grid(column=4, row=3)
        print("asdasdasdasdsadasdasdasd")
        # added resizing configs

    def resizeApp(self,e):
        # print("perinting n new ",e.width , self.f2.winfo_width())
        start = time.time()

        end = time.time()
        print("end ",end-start)
# def resizeApp(e):
#     print("perinting n new ",e.width )



def main():
    root = Tk()
    rw = ResizableWindow(root)
    root.wm_state('zoomed')
    # root.attributes('-zoomed', True)

    root.bind('<Configure>',rw.resizeApp)



    root.mainloop()
 
 
if __name__ == '__main__':
    main()