"""
Copyright (c) threewaysoft. All rights reserved.
Licensed under MIT License
Author: Jaeyong Seong
"""
from ResearchLibs.base_mathUtils import *
from ResearchLibs.DataStructure.GPS import GPSPoint
from collections.abc import Sequence

import math

class GPS_Calculator(object):
    R = 6378.137  # 지구의 반지름(KM)

    @staticmethod
    def TWO_GPS_Bearing(gps0: GPSPoint, gps1: GPSPoint) -> float:
        """ 두 GPS값이 있을 때 bearing 값을 계산한다. -> degree"""
        dLambda = CircularMATH.deg2rad(gps1._lon) - CircularMATH.deg2rad(gps0._lon)
        phi0 = CircularMATH.deg2rad(gps0._lat)
        phi1 = CircularMATH.deg2rad(gps1._lat)
        theta = math.atan2(math.sin(dLambda) * math.cos(phi1), math.cos(phi0) * math.sin(phi1) -
                           math.sin(phi0) * math.cos(phi1) * math.cos(dLambda))
        deg = CircularMATH.rad2deg(theta)
        if deg < 0:
            return 360 + deg
        else:
            return deg

    @staticmethod
    def GPS_Sorting(gps):
        """ GPS lat을 활용한 정렬 """
        if gps[1]._lat > gps[0]._lat or ((gps[1]._lat == gps[0]._lat) and (gps[1]._lon > gps[0]._lon)):
            gps1 = gps[1]
            gps0 = gps[0]
        else:
            gps1 = gps[0]
            gps0 = gps[1]
        return gps0, gps1

    @staticmethod
    def GPS_Bearing(gps, distance, bearing) -> GPSPoint:
        """ 기준 GPS를 알 때, bearing과 distance를 이용한 새 GPS 포인트 계산 """
        lat1, lon1 = gps._lat, gps._lon
        delta = distance / GPS_Calculator.R
        bearing = bearing / 180 * math.pi
        lat1 = lat1 / 180 * math.pi
        lon1 = lon1 / 180 * math.pi

        lat2 = math.asin(math.sin(lat1) * math.cos(delta) + math.cos(lat1) * math.sin(delta) * math.cos(bearing))
        lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(delta) * math.cos(lat1), math.cos(delta) - math.sin(lat1) * math.sin(lat2))

        lat2 = lat2 / math.pi * 180
        lon2 = lon2 / math.pi * 180

        return GPSPoint(0,0,0,lat2, lon2)

    @staticmethod
    def HarverSine(gps0, gps1):
        lat1, lon1, lat2, lon2 = gps0._lat, gps0._lon, gps1._lat, gps1._lon
        R = 6378.137  # 지구의 반지름(KM)
        dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180  # rad
        dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180  # rad
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * \
            math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return d * 1000