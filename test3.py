from tkinter import *
import webview
from multiprocessing import Process, Queue
import threading
# Create an instance of tkinter frame or window

# Create a GUI window to view the HTML content
webview.create_window('tutorialspoint', 'https://www.tutorialspoint.com')



p2 = Process(target=webview.start())
p2.start()
p2.join()