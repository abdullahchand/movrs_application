import json
from mvn.utils.multiview import Camera
# Using readlines()
import numpy as np




class Calib:
    def __init__(self,path,num_cameras) -> None:
        self.path = path
        self.num_cameras = num_cameras

    def converter(self):
        file = open(self.path+"camera.calib", 'r')
        Lines = file.readlines()
        
        count = 0
        # Strips the newline character
        get_extrinsics=0
        get_intrinsics=0
        extrinsics_array = []
        intrinsics_array =[]
        translation_array = []
        intrinsics_count = 0
        camera_count=0
        for line in Lines:
            new_line = line.strip()

            if  '#' == new_line[0]:
                if 'extrinsics' in new_line:
                    get_extrinsics = 1
                    get_intrinsics = 0

                if 'intrinsics' in new_line:
                    get_intrinsics = 1
                    get_extrinsics = 0

                if get_extrinsics == 1 and 'extrinsics' not in new_line:
                    arr = new_line.split()
                    translation_array.append(arr[4]) 
                    del arr[4]

                    del arr[0]
                    extrinsics_array.append(arr)


                if get_intrinsics == 1  and 'intrinsics' not in new_line:
                    arr = new_line.split()
                    del arr[0]
                    print(arr)
                    intrinsics_array.append(arr)
                    intrinsics_count +=1
                    print(intrinsics_count)
                    if intrinsics_count == 3:
                        camera_count +=1

                        x = {
                        "r": np.array(extrinsics_array).astype(np.float).tolist(),
                        "t": np.array(translation_array).astype(np.float).tolist(),
                        "K": np.array(intrinsics_array).astype(np.float).tolist()
                        }

                        # convert into JSON:
                        y = json.dumps(x)
                        # Writing to sample.json
                        with open("data_stream/camera/"+str(camera_count-1)+".json", "w") as outfile:
                            outfile.write(y)
                        print ('----------------------------------------------------')
                        extrinsics_array = []
                        intrinsics_array =[]
                        translation_array = []
                        intrinsics_count = 0

            
    def get_camera_matrix(self):
        camera = []
        for i in range(0,self.num_cameras+1):
            with open("data_stream/camera/"+str(i)+".json") as f:
                data = json.load(f)
                camera.append(Camera(data['r'], (data['t']), data['K'], str(i)).projection)
        return camera
        
            