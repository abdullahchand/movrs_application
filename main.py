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
        self.parent = parent
        self.f1_style = ttk.Style()

        self.f1_style.configure('My.TFrame', background='#334353')

        self.f1 = ttk.Frame(self.parent, style='My.TFrame' )  # added padding
        # main_video is for main video
        self.main_video = ttk.Frame(self.f1 )




        self.bottom_frames = ttk.Frame(self.f1 )

        self.bottom_video_list = ttk.Frame(self.bottom_frames, style='My.TFrame' )


        self.tabControl0 = ttk.Notebook(self.f1)
        self.tab10 = ttk.Frame(self.tabControl0)
        self.tab20 = ttk.Frame(self.tabControl0)
        
        self.tabControl0.add(self.tab10, text ='Tab 1')
        self.tabControl0.add(self.tab20, text ='Tab 2')
        # self.tabControl.pack(expand = 1, fill ="both")

        ttk.Label(self.tab10, text ="Welcome to \GeeksForGeeks").grid(column = 0,row = 0,padx = 30,pady = 30)  
        ttk.Label(self.tab20,
                text ="Lets dive into the\world of computers").grid(column = 0,row = 0, padx = 30,pady = 30)




        self.tabControl = ttk.Notebook(self.f1)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.tab1, text ='Tab 1')
        self.tabControl.add(self.tab2, text ='Tab 2')
        # self.tabControl.pack(expand = 1, fill ="both")

        ttk.Label(self.tab1, text ="Welcome to GeeksForGeeks").grid(column = 0,row = 0,padx = 30,pady = 30)  
        ttk.Label(self.tab2,text ="Lets dive into theworld of computers").grid(column = 0,row = 0, padx = 30,pady = 30)


        self.tabControl2 = ttk.Notebook(self.bottom_video_list)
        self.tab12 = ttk.Frame(self.tabControl2)
        self.tab22 = ttk.Frame(self.tabControl2)
        
        self.tabControl2.add(self.tab12, text ='Live View')
        self.tabControl2.add(self.tab22, text ='Preview')

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.f1.columnconfigure(0, weight=3)
        self.f1.columnconfigure(1, weight=3)
        self.f1.columnconfigure(2, weight=3)
        self.f1.columnconfigure(3, weight=4)

        # self.f1.rowconfigure(1, weight=3)
        self.f1.rowconfigure(1, weight=3)
        self.f1.rowconfigure(2, weight=3)
        self.f1.rowconfigure(3, weight=5)

        self.bottom_frames.columnconfigure(1, weight=3)
        self.bottom_frames.columnconfigure(2, weight=3)
        self.bottom_frames.columnconfigure(3, weight=3)
        self.bottom_frames.columnconfigure(4, weight=3)
        self.bottom_frames.rowconfigure(0, weight=1)


        
        self.main_video.columnconfigure(0, weight=1)
        self.main_video.rowconfigure(0, weight=1)
        self.bottom_frames.columnconfigure(0, weight=1)
        self.bottom_frames.rowconfigure(0, weight=1)
        self.bottom_video_list.columnconfigure(0, weight=1)
        self.bottom_video_list.rowconfigure(0, weight=1)
        # self.tab12.columnconfigure(0, weight=1)
        # self.tab12.rowconfigure(0, weight=1)
        self.f1.grid(column=0 , row=0, sticky=(N, S, E, W))  # added sticky
        self.main_video.grid(column=0,row=0, columnspan=3, rowspan=3, sticky=(N, S, E, W))  # added sticky

        self.bottom_frames.grid(column=0,row=3, columnspan=5, rowspan=1, sticky=(N, S, E, W))  # Bottom

        self.bottom_video_list.grid(column=0,row=0, columnspan=5, rowspan=1, sticky=(N, S, E, W))  # Bottom
        self.tabControl0.grid(column=3, row=1, columnspan=2, sticky=(N, E, W, S), padx=5,pady=5)  # added sticky, padx
        self.tabControl.grid(column=3, row=0, columnspan=2, sticky=(N, E, W), padx=5,pady=5)  # added sticky, padx
        self.tabControl2.grid(column=0, row=0, columnspan=4, sticky=(N, E, W, S), padx=5,pady=5)  # added sticky, padx

       

        self.img = ImageTk.PhotoImage(Image.open("2.jpg"))
        self.canvas= Canvas( self.main_video)
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas.grid(column=0 ,row =0 ,sticky="NSEW")


        # button1=ttk.Button( self.tab12, text="button1")
        # button1.grid(pady = 2,row=0,column=0)

        # button2=ttk.Button( self.tab12, text="button2")
        # button2.grid(pady = 2,row=0,column=1)

        # button3=ttk.Button( self.tab12, text="button3")
        # button3.grid(pady = 2,row=0,column=2)

        # button4=ttk.Button( self.tab12, text="button4")
        # button4.grid(pady = 2,row=0,column=3)

        # button5=ttk.Button( self.tab12, text="button5")
        # button5.grid(pady = 2,row=0,column=4)

        # button6=ttk.Button( self.tab12, text="button1")
        # button6.grid(pady = 2,row=1,column=0)

        # button7=ttk.Button( self.tab12, text="button2")
        # button7.grid(pady = 2,row=1,column=1)

        # button8=ttk.Button( self.tab12, text="button3")
        # button8.grid(pady = 2,row=1,column=2)

        # button9=ttk.Button( self.tab12, text="button4")
        # button9.grid(pady = 2,row=1,column=3)

        # button10=ttk.Button( self.tab12, text="button5")
        # button10.grid(pady = 2,row=1,column=4)

        self.img1 = ImageTk.PhotoImage(Image.open("3.jpg"))
        self.canvas1= Canvas( self.tab12)
        self.canvas1.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas1.grid(column=0 ,row =0 ,sticky="NW", columnspan=1)


        
        self.img2 = ImageTk.PhotoImage(Image.open("1.jpg"))
        self.canvas2= Canvas( self.tab12)
        self.canvas2.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas2.grid(column=1 ,row =0 ,sticky="NW")

        
        self.img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
        self.canvas3= Canvas( self.tab12)
        self.canvas3.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas3.grid(column=2 ,row =0 ,sticky="NW", columnspan=1)

        self.img4 = ImageTk.PhotoImage(Image.open("3.jpg"))
        self.canvas4= Canvas( self.tab12)
        self.canvas4.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas4.grid(column=3 ,row =0 ,sticky="NW", columnspan=1)

        self.img5 = ImageTk.PhotoImage(Image.open("2.jpg"))
        self.canvas5= Canvas( self.tab12)
        self.canvas5.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas5.grid(column=4 ,row =0 ,sticky="NSEW", columnspan=1)

        self.img6 = ImageTk.PhotoImage(Image.open("1.jpg"))
        self.canvas6= Canvas( self.tab12)
        self.canvas6.create_image(0.5,0.5,anchor=NW,image=self.img)
        self.canvas6.grid(column=5 ,row =0 ,sticky="NSEW", columnspan=1)
        self.img6 = Image.open("1.jpg")
        self.resized_img6 = self.img6.resize((100,100),Image.ANTIALIAS)
        self.new_bg6 = ImageTk.PhotoImage(self.resized_img6 )
        # # self.canvas6.create_image(0.5,0.5,anchor=NW,image=self.new_bg6)
        # button1=ttk.Button( self.tab12,image = self.new_bg6, text="button1")
        # button1.grid(pady = 2,row=0,column=0)

        # button2=ttk.Button( self.tab12,image = self.new_bg6, text="button2")
        # button2.grid(pady = 2,row=0,column=1)

        # button3=ttk.Button( self.tab12,image = self.new_bg6, text="button3")
        # button3.grid(pady = 2,row=0,column=2)

        # button4=ttk.Button( self.tab12,image = self.new_bg6, text="button4")
        # button4.grid(pady = 2,row=0,column=3)

        # button5=ttk.Button( self.tab12,image = self.new_bg6, text="button5")
        # button5.grid(pady = 2,row=0,column=4)

        # button6=ttk.Button( self.tab12,image = self.new_bg6, text="button1")
        # button6.grid(pady = 2,row=1,column=0)

        # button7=ttk.Button( self.tab12,image = self.new_bg6, text="button2")
        # button7.grid(pady = 2,row=1,column=1)

        # button8=ttk.Button( self.tab12,image = self.new_bg6, text="button3")
        # button8.grid(pady = 2,row=1,column=2)

        # button9=ttk.Button( self.tab12,image = self.new_bg6, text="button4")
        # button9.grid(pady = 2,row=1,column=3)

        # button10=ttk.Button( self.tab12,image = self.new_bg6, text="button5")
        # button10.grid(pady = 2,row=1,column=4)



        self.scrollbar = Scrollbar( self.tab12, orient='horizontal')
        self.scrollbar.config()


    def resizeApp(self,e):

        start = time.time()
        self.img = Image.open("1.jpg")
        self.resized_img = self.img.resize((self.main_video.winfo_width(),self.main_video.winfo_height()),Image.ANTIALIAS)
        self.new_bg = ImageTk.PhotoImage(self.resized_img )
        self.canvas.create_image(0.5,0.5,anchor=NW,image=self.new_bg)
        # print("tab12",self.tab12.winfo_width())
        self.sample_width = int(( self.tab12.winfo_width()/4)/2)
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