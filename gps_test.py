import numpy as np
import sys
import math
from DataStructure.Vector2D import Vector2D
from DataStructure.GPS import GPSPoint
from DataStructure.DataConverter import *
from base_mathUtils import *
from GISLib.GIS_GPS_Calculator import GPS_Calculator

def GPS_Mapping_Pipeline():
    ## 0. 기준 GPS값 매핑
    gps_file_name = "my_gps_2.txt"
    lines = []
    with open(gps_file_name, 'r') as f:
        for index, i in enumerate(f.readlines()):
            lines.append(i)

    my_GPS = []
    for index, l in enumerate(lines):
        split_data = np.array(l.split(",")).astype(np.float32)
        if len(split_data) == 5:
            my_GPS.append(GPSPoint(split_data[0], split_data[1], split_data[2], split_data[3], split_data[4]))
        else:
            raise NotImplementedError

    # 1. 기준 GPS값 정렬 및 bearing 계산
    g0 = my_GPS[0]
    g1 = my_GPS[1]
    g0, g1 = GPS_Calculator.GPS_Sorting([g0, g1])
    base_bearing_deg = GPS_Calculator.TWO_GPS_Bearing(g0, g1)
    print(base_bearing_deg)
    print(GPS_Calculator.HarverSine(g0, g1))

    # 2. 기준 GPS값과 타겟 포인트 사이의 bearing 계산
    t = Vector2D(-10, 10, 11.599462)
    p0 = GPS2Vector2D(g0)
    p1 = GPS2Vector2D(g1)

    base_vector = p1 - p0
    target_vector = t - p0

    target_bearing = VectorMATH.vec_clockwise_angle(base_vector, target_vector)
    print(g0, g1)
    print(CircularMATH.rad2deg(target_bearing))


GPS_Mapping_Pipeline()
# g0 = GPSPoint(0,0,0,34.33298587287949, 134.0480806664525)
# g1 = GPSPoint(0,0,0, 34.3325498987043, 134.04801339215328)
# print(CircularMATH.rad2deg(GPS_Calculator.TWO_GPS_Bearing(g0, g1)) + 360)