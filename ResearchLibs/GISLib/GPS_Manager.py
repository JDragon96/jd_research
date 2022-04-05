from ResearchLibs.GISLib.GIS_GPS_Calculator import GPS_Calculator
from ResearchLibs.DataStructure.DataConverter import *
import numpy as np

class GPSManager:
    gps0 = None
    gps1 = None
    gps_point0 = None
    gps_point1 = None
    base_bearing_deg = None
    base_vector = None
    base_distance_using_gps = None
    base_distance_using_point = None

    def __init__(self, filename=None):
        if filename != None:
            self.gps_file_name = filename

            lines = []
            with open(self.gps_file_name, 'r') as f:
                for index, i in enumerate(f.readlines()):
                    lines.append(i)
                    
            if len(lines) != 2:
                raise NotImplementedError("GPS 기준값을 두 개로 설정해주세요.\n"
                                          "fotmat=> [x, y, z, lat, lon]\n"
                                          "0, 10, 0, 34.332,134.0480\n"
                                          "0, 0, 0, 34.332,134.0480\n")

            my_GPS = []
            for index, l in enumerate(lines):
                split_data = np.array(l.split(",")).astype(np.float32)
                if len(split_data) == 5:
                    my_GPS.append(GPSPoint(split_data[0], split_data[1], split_data[2], split_data[3], split_data[4]))
                else:
                    raise NotImplementedError("GPS 기준값이 올바르지 않습니다.")

            if len(my_GPS) != 2:
                raise NotImplementedError("GPS값이 올바르게 정렬되지 않았습니다. delimiter는 ',' 입니다.")

            self.gps0 = my_GPS[0]
            self.gps1 = my_GPS[1]

        else:
            raise FileNotFoundError("GPS 기준 파일을 찾을 수 없습니다.")

    def Manager_Setting_Pipeline(self, debug=False):
        self.gps0, self.gps1 = GPS_Calculator.GPS_Sorting([self.gps0, self.gps1])
        self.gps_point0 = GPS2Vector2D(self.gps0)
        self.gps_point1 = GPS2Vector2D(self.gps1)
        self.base_bearing_deg = GPS_Calculator.TWO_GPS_Bearing(self.gps0, self.gps1)
        self.base_vector = self.gps_point1 - self.gps_point0
        self.base_distance_using_gps = GPS_Calculator.HarverSine(self.gps0, self.gps1)
        self.base_distance_using_point = self.gps_point0.vector_distance_2D(self.gps_point1)
        if debug:
            print(f"[Manager Parameter Setting Pipeline]\n"
                  f"gps0 : {self.gps0}\n"
                  f"gps1 : {self.gps1}\n"
                  f"base bearing(deg) : {self.base_bearing_deg}\n"
                  f"base distance(gps) : {self.base_distance_using_gps}\n"
                  f"base distance(point) : {self.base_distance_using_point}\n"
                  f"distnace ratio : {self.check_distance_ratio_between_gps_and_point()}\n")

    def getBearing(self):
        if self.base_bearing_deg is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.base_bearing_deg

    def getGPS0(self):
        if self.gps0 is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.gps0

    def getGPS1(self):
        if self.gps1 is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.gps1

    def getGPS_Point0(self):
        if self.gps_point0 is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.gps_point0

    def getGPS_Point1(self):
        if self.gps_point1 is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.gps_point1

    def getBaseVector(self):
        if self.base_vector is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.base_vector

    def getBaseDistanceUsingGPS(self):
        if self.base_distance_using_gps is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.base_distance_using_gps

    def getBaseDistanceUsingPoint(self):
        if self.base_distance_using_point is None:
            raise NotImplementedError("GPS 정렬을 먼저 해야합니다.")
        return self.base_distance_using_point

    def check_distance_ratio_between_gps_and_point(self):
        if self.base_distance_using_point is None or self.base_distance_using_gps is None :
            raise NotImplementedError("GPS값이 올바르게 입력되지 않았습니다.")
        return self.base_distance_using_gps / self.base_distance_using_point

    def getNewGPS_Using_Bearing_and_Distance(self, distance, bearing):
        return GPS_Calculator.GPS_Bearing(self.gps0, distance, bearing)

    def lat_scaling(self):
        return GPS_Calculator.HarverSine(GPSPoint(0,0,0,36,120), GPSPoint(0,0,0,37,120))

    def lon_scaling(self):
        return GPS_Calculator.HarverSine(GPSPoint(0,0,0,36,120), GPSPoint(0,0,0,36,121))


if __name__=="__main__":
    GPSManager()