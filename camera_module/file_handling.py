import os
import json
from config import FILE_PATH

file_path = FILE_PATH


def read_file():
    try:
        f = open(file_path, "r")
        calibration_values = f.read()
        f.close()
        # print(calibration_values)
        return json.dumps(calibration_values)
    except Exception as e:
        print(e)
        return {"type": "", "value": "", "cam_no": "", "error": "true"}


def write_file(data):
    with open(file_path, "w+") as outfile:
        json.dump(data, outfile)


def delete_file():
    os.remove(file_path)
