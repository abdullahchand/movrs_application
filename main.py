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
 
class ResizableWindow:
    def __init__(self, parent):
        # root = parent 
        self.parent = parent

        #creating menu_bar for top 
        self.menubar = Menu(self.parent )  

        self.file = Menu(self.menubar, tearoff=0)  
        self.file.add_command(label="New")  
        self.file.add_command(label="Open")  
        self.file.add_command(label="Save")  
        self.file.add_command(label="Save as...")  
        self.file.add_command(label="Close")  
        self.file.add_separator()  
        self.file.add_command(label="Exit", command=self.parent )  
        self.menubar.add_cascade(label="File", menu=self.file)  

        self.edit = Menu(self.menubar, tearoff=0)  
        self.edit.add_command(label="Undo")  
        self.edit.add_separator()  
        self.edit.add_command(label="Cut")  
        self.edit.add_command(label="Copy")  
        self.edit.add_command(label="Paste")  
        self.edit.add_command(label="Delete")  
        self.edit.add_command(label="Select All")  
        self.menubar.add_cascade(label="Edit", menu=self.edit)  

        help = Menu(self.menubar, tearoff=0)  
        help.add_command(label="About")  
        self.menubar.add_cascade(label="Help", menu=help)  
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




        self.img = ImageTk.PhotoImage(Image.open("2.jpg"))
        self.canvas= Canvas( self.main_video)
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas.grid(column=0 ,row =0 ,sticky="NSEW")



        self.img1 = ImageTk.PhotoImage(Image.open("3.jpg"))
        self.canvas1= Canvas( self.bottom_tab_1)
        self.canvas1.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas1.grid(column=0 ,row =0 ,sticky="NW", columnspan=1)


        
        self.img2 = ImageTk.PhotoImage(Image.open("1.jpg"))
        self.canvas2= Canvas( self.bottom_tab_1)
        self.canvas2.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas2.grid(column=1 ,row =0 ,sticky="NW")

        
        self.img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
        self.canvas3= Canvas( self.bottom_tab_1)
        self.canvas3.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas3.grid(column=2 ,row =0 ,sticky="NW", columnspan=1)

        self.img4 = ImageTk.PhotoImage(Image.open("3.jpg"))
        self.canvas4= Canvas( self.bottom_tab_1)
        self.canvas4.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas4.grid(column=3 ,row =0 ,sticky="NW", columnspan=1)

        self.img5 = ImageTk.PhotoImage(Image.open("2.jpg"))
        self.canvas5= Canvas( self.bottom_tab_1)
        self.canvas5.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas5.grid(column=4 ,row =0 ,sticky="NSEW", columnspan=1)

        self.img6 = ImageTk.PhotoImage(Image.open("1.jpg"))
        self.canvas6= Canvas( self.bottom_tab_1)
        self.canvas6.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas6.grid(column=5 ,row =0 ,sticky="NSEW", columnspan=1)


        
        self.main_video.columnconfigure(0, weight=1)
        self.main_video.rowconfigure(0, weight=1)

        self.bottom_video_list.columnconfigure(0, weight=1)
        self.bottom_video_list.rowconfigure(0, weight=1)

        self.main_window.grid(column=0 , row=0, sticky=(N, S, E, W))  # added sticky
        self.main_video.grid(column=0,row=0, columnspan=3, rowspan=3, sticky=(N, S, E, W))  # added sticky

        self.bottom_frames.grid(column=0,row=3, columnspan=5, rowspan=1, sticky=(N, S, E, W))  # Bottom

        self.bottom_video_list.grid(column=0,row=0, columnspan=5, rowspan=1, sticky=(N, S, E, W))  # Bottom
        

       




    def resizeApp(self,e):

        start = time.time()
        self.img = Image.open("1.jpg")
        self.resized_img = self.img.resize((self.main_video.winfo_width(),self.main_video.winfo_height()),Image.ANTIALIAS)
        self.new_bg = ImageTk.PhotoImage(self.resized_img )
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.new_bg)
        # print("bottom_tab_1",self.bottom_tab_1.winfo_width())
        self.sample_width = int(( self.bottom_tab_1.winfo_width()/4)/2)
        self.img1 = Image.open("2.jpg")
        self.resized_img1 = self.img1.resize((self.sample_width,self.sample_width),Image.ANTIALIAS)
        self.new_bg1 = ImageTk.PhotoImage(self.resized_img1 )
        self.canvas1.create_image(0.5,0.5,anchor=NW,image=self.new_bg1)

        self.img2 = Image.open("3.jpg")
        self.resized_img2 = self.img2.resize((self.sample_width,self.sample_width),Image.ANTIALIAS)
        self.new_bg2 = ImageTk.PhotoImage(self.resized_img2 )
        self.canvas2.create_image(0.5,0.5,anchor=NW,image=self.new_bg2)

        self.img3 = Image.open("1.jpg")
        self.resized_img3 = self.img3.resize((self.sample_width,self.sample_width),Image.ANTIALIAS)
        self.new_bg3 = ImageTk.PhotoImage(self.resized_img3 )
        self.canvas3.create_image(0.5,0.5,anchor=NW,image=self.new_bg3)

        self.img4 = Image.open("1.jpg")
        self.resized_img4 = self.img4.resize((self.sample_width,self.sample_width),Image.ANTIALIAS)
        self.new_bg4 = ImageTk.PhotoImage(self.resized_img4 )
        self.canvas4.create_image(0.5,0.5,anchor=NW,image=self.new_bg4)

        self.img5 = Image.open("1.jpg")
        self.resized_img5 = self.img5.resize((self.sample_width,self.sample_width),Image.ANTIALIAS)
        self.new_bg5 = ImageTk.PhotoImage(self.resized_img5 )
        self.canvas5.create_image(0.5,0.5,anchor=NW,image=self.new_bg5)






        # for x in range(6):
        #     print(x)

        # end = time.time()
        # print("end ",end-start)




def main():
    root = Tk()
    rw = ResizableWindow(root)
    # root.wm_state('zoomed')
    root.attributes('-zoomed', True)

    root.bind('<Configure>',rw.resizeApp)



    root.mainloop()
 
 
if __name__ == '__main__':
    main()