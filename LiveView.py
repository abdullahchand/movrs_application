from tkinter import *
import tkinter
from PIL import Image, ImageTk






root =Tk()
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
    

main_screen_width = root.winfo_screenwidth()
main_screen_height = root.winfo_screenheight()-65
root.geometry("%dx%d" % (main_screen_width, main_screen_height))
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
  

root.config(menu=menubar)  




Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=5)
Grid.columnconfigure(root,1,weight=1)


image = Image.open("3.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(main_video_frame, image = photo)
label.grid(row=0 ,column=0 , sticky="nwes")
Grid.rowconfigure(main_video_frame,0,weight=1)
Grid.columnconfigure(main_video_frame,0,weight=5)


 

root.mainloop()