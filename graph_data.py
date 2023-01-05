import json
import asyncio
import websockets
import socket
from converter.bvh_converter.bvhplayer_skeleton import ReadBVH, process_bvhnode, Skeleton, process_bvhkeyframe
import time
import math
from multiprocessing import Process, Queue
import functools
# from check_ports import started_sockets_ports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


# Remove port if needed
total_socket = []


class GraphData:
	def __init__(self):
		self.result_array = Queue()
		self.time_now = Queue()
		self.joints_name = Queue()
		self.bvh_data = Queue()
		self.bvh_header_data = Queue()
		self.bvh_header = ""



	def start_proces(self):
		p = Process(target=self.echo)
		p.start()

	def echo(self):

		i = 1
		HOST = "127.0.0.1"  # The server's hostname or IP address
		PORT = 2110   

		hierarchy_made = False
		my_bvh = None
		hips = None
		frame_counter = 0
		old= {
			"Time": 0,
			"LeftHandEnd.X": 0,
			"LeftHandEnd.Y": 0,
			"LeftHandEnd.Z": 0,
		} 


		header_confirmed = 0
		joints_to_read = []
		total_joints = len(joints_to_read)

		# LeftArm.Z RightArm.X Hips.Y

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((HOST, PORT))
			PORT = 2110 # The port used by the server
			connection_state = True
			socket_data = []
			while True:
				data1 = s.recv(100000)
				line = data1.decode()
				# print(line)
				# my_bvh = process_bvhfile(line)
				if not hierarchy_made:
					my_bvh = ReadBVH(line)  # Doesn't actually read the file, just creates
					# a readbvh object and sets up the file for
					# reading in the next line.
					my_bvh.read()  # Reads and parses the file.

					hips = process_bvhnode(my_bvh.root)  # Create joint hierarchy
					
					hierarchy_made = True
					self.bvh_header = str(line)
					# print(str(line))
				else: 
					my_bvh.read_motion(line,frame_counter,0.0166667) 

					# print("Building skeleton...", frame_counter)
					myskeleton = Skeleton(hips, keyframes=my_bvh.keyframes, frames=my_bvh.frames, dt=my_bvh.dt)
					# print(myskeleton.frames)
					# if myskeleton.frames == 0:
					# 	continue
					# for i in range(myskeleton.frames):
						# print("Time : ",myskeleton.dt * i)
					process_bvhkeyframe(myskeleton.keyframes[frame_counter], myskeleton.root, my_bvh.dt * frame_counter)
					header, frames = myskeleton.get_frames_worldpos(frame_counter)
					time = 0

					if header_confirmed ==0 :
						final_header = header
						header_confirmed =1
						final_header.remove("Time")
						total_joints = len(final_header)

						for i in range(0, total_joints):
							array_value = final_header[i].split(".", 1)[0]
							if not array_value in joints_to_read:
								joints_to_read.append(array_value)
						total_joints = len(joints_to_read)
						for i in range(0, total_joints):
							globals()[joints_to_read[i]] = 2
							globals()[joints_to_read[i]+'_old'] = {
								"Time": 0,
								joints_to_read[i]+".X": 0,
								joints_to_read[i]+".Y": 0,
								joints_to_read[i]+".Z": 0,
							} 
					return_value = {
						"Joints" : joints_to_read,
						"Velocity" : 0,
					}
					final_reasult =[]
					for i in range(0, total_joints):
						difference, time_frame =  self.getDiffrences( joints_to_read[i] , header , frames , old)
						velocity =  self.getVelocity( joints_to_read[i] , difference , 0.0166667)
						final_reasult.append(velocity)
						return_value["Time"] = time_frame
					return_value ['result'] = final_reasult
					return_value ['bvh'] = line
					socket_data.append(return_value)
					self.result_array.put(final_reasult)
					frame_counter += 1
					self.bvh_data.put(line)
					self.joints_name.put(joints_to_read)
					self.bvh_header_data.put(self.bvh_header)

					self.time_now.put(return_value["Time"])


	def getDiffrences(self,joint_name , header , frames, old):
		Time = frames[0][0]
		new_x = frames[0][header.index(joint_name+".X")] 
		new_y = frames[0][header.index(joint_name+".Y")]
		new_z = frames[0][header.index(joint_name+".Z")]
		differnce = {
			"Time": frames[0][0],
			joint_name+".X": new_x - globals()[joint_name+"_old"][joint_name+".X"],
			joint_name+".Y": new_y - globals()[joint_name+"_old"][joint_name+".Y"],
			joint_name+".Z": new_z - globals()[joint_name+"_old"][joint_name+".Z"],
		}
		globals()[joint_name+"_old"] = {
			"Time": Time,
			joint_name+".X": new_x,
			joint_name+".Y": new_y,
			joint_name+".Z": new_z,
		}
		return differnce , Time

	def getVelocity(self,joint_name , differnce,dt):
		distance = math.sqrt((differnce[joint_name+".X"]**2+differnce[joint_name+".Y"]**2+differnce[joint_name+".Z"]**2))
		return distance * dt


