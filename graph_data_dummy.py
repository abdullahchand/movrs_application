import json
import asyncio
import time
import math
from multiprocessing import Process, Queue
import functools
# from check_ports import started_sockets_ports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import random


# Remove port if needed
total_socket = []


class GraphData:
	def __init__(self):
		self.result_array = Queue()
		self.time_now = Queue()
		self.joints_name = Queue()
		self.bvh_data = Queue()
		self.count=0


	def start_proces(self):
		p = Process(target=self.echo)
		p.start()

	def echo(self):
		while True:
			randomlist = []
			for i in range(0,5):
				n = random.randint(1,30)
				randomlist.append(n)
			self.result_array.put(randomlist)
			self.count += 1
			self.time_now.put(self.count)
			self.bvh_data.put("bvh")


i = 0	
# multiprocessing = []
loop =[]

# started_sockets_ports()


obj = GraphData()






fig = plt.figure(figsize=(6, 3))
x = [0]
y = [0]
y2 = [0]
y3 = [0]
ln, = plt.plot(x, y, '-')
ln2, = plt.plot(x, y, '-')
ln3, = plt.plot(x, y, '-')
plt.axis([0, 50, 0, 20])
 
def update(frame):
    # y.append(randrange(0, 10))
    # y3.append(randrange(5, 15))
    # y2.append(randrange(10, 19))
	result = obj.result_array.get()
	time_now  = obj.time_now.get()
	x.append(time_now)
	y.append(result[0])
	y2.append(result[1])
	y3.append(result[2])
	time.sleep(0.1)

	if(time_now>50):
		plt.axis([0, 1000, 0, 20])
		plt.subplots()
	if(time_now<5):
		ln.set_data(x, y) 
		ln2.set_data(x, y3) 
		ln3.set_data(x, y2) 
		return [ln,ln2,ln3]
	else:
		ln.set_data(x, y) 
		return [ln]
		






if __name__ == '__main__':

	obj.start_proces()
	animation = FuncAnimation(fig, update, interval=1,blit=True)
	plt.show()





# obj.echo()

