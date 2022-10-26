from tkinter import *
import tkinter

root =Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()-65

# label= Label(root, text= "Movrs VS Panel", font=('Times New Roman bold',20))
# label.grid(row = 0 , column=0)



videoframe1 = tkinter.Frame(root ,width =width -(width/4),bg="red" , height=height)
videoframe1.grid(row=1 ,column=0 , sticky="N")

secondgrid = tkinter.Frame(root ,width =width -(width/4) , height=height)
secondgrid.grid(row=1 ,column=1 , sticky="N")

videoframe1 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="blue" , height=height/7)
videoframe1.grid(row=1 ,column=1 , sticky="N")
videoframe2 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="yellow" , height=height/7)
videoframe2.grid(row=2 ,column=1, sticky="N")
videoframe3 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="blue" , height=height/7)
videoframe3.grid(row=3 ,column=1, sticky="N")
videoframe4 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="yellow" , height=height/7)
videoframe4.grid(row=4 ,column=1, sticky="N")
remainingHeight = height - (height/7)*4

buttons = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="green" , height=remainingHeight)
buttons.grid(row=5 ,column=1)







videoframe5 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="yellow" , height=height/7)
videoframe5.grid(row=1 ,column=2, sticky="N")
videoframe6 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="blue" , height=height/7)
videoframe6.grid(row=2 ,column=2, sticky="N")
videoframe7 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="yellow" , height=height/7)
videoframe7.grid(row=3 ,column=2, sticky="N")
videoframe8 = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="blue" , height=height/7)
videoframe8.grid(row=4 ,column=2, sticky="N")

buttons = tkinter.Frame(secondgrid ,width =(width/4)/2,bg="green" , height=remainingHeight)
buttons.grid(row=5 ,column=2)








# main_screen = Label(root , text="",bg="black",height= height, width=int(120),fg='white').grid(row = 1 , column=0, sticky="ns", padx=10, pady=10)

# screen1 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(column = 1, row = 10, columnspan = 2, sticky = tkinter.S+tkinter.E)

# screen2 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 2 , column=1 , sticky="ne", padx=10, pady=10)

# screen3 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 3 , column=1 , sticky="ne", padx=10, pady=10)

# screen4 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 4 , column=1 , sticky="ne", padx=10, pady=10)

# screen5 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 1 , column=2 , sticky="ne", padx=10, pady=10)

# screen6 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 2 , column=2 , sticky="ne", padx=10, pady=10)

# screen7 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 3 , column=2 , sticky="ne", padx=10, pady=10)

# screen8 = Button(root , text="",bg="black",height= 5, width=30 ,fg='white').grid(row = 4 , column=2 , sticky="ne", padx=10, pady=10)



# main_screen = Label(root , text="",bg="black",height= height, width=int(140)).grid(row = 1 , column=0)

# screen1 = Button(root , text="",bg="black",height= 30, width=30).grid(row = 1 , column=1)

# screen2 = Button(root , text="",bg="black",height= 30, width=30).grid(row = 1 , column=1)

# screen3 = Button(root , text="",bg="black",height= 30, width=30).grid(row = 1 , column=1)

# screen4 = Button(root , text="",bg="black",height= 30, width=30).grid(row = 1 , column=1)

def resizeApp(self,e):
    print("perinting n new ",e.width, e.videoframe1.width )

root.bind('<Configure>',resizeApp)
root.mainloop()