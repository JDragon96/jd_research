import pye57.scan_header
import laspy
import os
import numpy as np

from ResearchLibs.DataStructure.Vector2D import Vector2D

def load_las(filepath):
    data = laspy.file.File(filepath, mode='r')
    scaleX = data.header.scale[0]
    scaleY = data.header.scale[1]
    scaleZ = data.header.scale[2]
    offset = data.header.offset

    red = data.red * 255 / 65535
    blue = data.blue * 255 / 65535
    green = data.green * 255 / 65535

    my_data = np.vstack([data.X * scaleX + offset[0],
                         data.Y * scaleY + offset[1],
                         data.Z * scaleZ + offset[2],
                         red,
                         blue,
                         green])
    las_header = data.header
    return my_data, las_header

def save_las(data, header, filename):
    with laspy.file.File(f"{filename}.las", mode="w", header=header) as lasfile:
        lasfile.header.offset = header.offset
        lasfile.header.scale = header.scale
        # lasfile.header.scale = [sfactor, sfactor, sfactor]

        lasfile.x = data[0]
        lasfile.y = data[1]
        lasfile.z = data[2]
        lasfile.red = data[3]
        lasfile.green = data[4]
        lasfile.blue = data[5]

def load_e57(filepath):
    e57 = pye57.E57(filepath)
    data = e57.read_scan(0, intensity=True, colors=True, ignore_missing_fields=True)
    x = data["cartesianX"]
    y = data["cartesianY"]
    z = data["cartesianZ"]
    r = data["colorRed"]
    g = data["colorGreen"]
    b = data["colorBlue"]
    my_data = np.vstack([x, y, z, r, g, b])
    return my_data, e57.get_header(0)

def save_e57(filename):
    pass

def load_txt(filepath):
    pass
def save_txt(filename):
    pass



class DATA_HUB:
    load_file_name = None
    load_extension = None
    save_file_name = None
    header = None
    debug = None

    def __init__(self, load_name, save_name, debug):
        self.load_file_name = load_name
        self.save_file_name = save_name
        self.debug = debug
        self.load_extension = os.path.splitext(load_name)[1]

    def DATA_load(self):
        if self.load_extension == ".las":
            data, self.header = load_las(self.load_file_name)
        elif self.load_extension == ".e57":
            data, self.header = load_e57(self.load_file_name)
        else:
            data = load_txt(self.load_file_name)

        data = np.array(data).T
        if self.debug:
            print(f"[DATA_HUB]\n"
                  f"filename : {self.load_file_name}\n"
                  f"extension : {self.load_extension}\n"
                  f"data shape : {np.shape(data)}\n")


        ## nparray -> Vector2D
        new_data = []
        for p in data:
            v = Vector2D(p[0], p[1], p[2])
            v.setColor(p[3], p[4], p[5])
            new_data.append(v)


        return new_data

    def DATA_save(self, data):
        if self.debug:
            print(f"[Data save]\n"
                  f"save name : {self.save_file_name}\n"
                  f"extension : {self.load_extension}\n"
                  f"data save : {np.shape(data)}\n")

        if self.load_extension == ".las":
            save_las(data, self.header, self.save_file_name)
        elif self.load_extension == ".e57":
            save_e57(data)
        else:
            save_txt(data)