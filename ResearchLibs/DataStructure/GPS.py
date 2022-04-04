"""
Copyright (c) threewaysoft. All rights reserved.
Licensed under MIT License
Author: Jaeyong Seong
"""
from base_mathUtils import *

class GPSPoint(object):
    _x = 0
    _y = 0
    _z = 0
    _lat = 0
    _lon = 0

    def __init__(self,x,y,z,lat,lon):
        self._x = x
        self._y = y
        self._z = z
        self._lat = lat
        self._lon = lon

    def __repr__(self):
        return (f"GPSPoint<x :{self._x} / y :{self._y} / z :{self._z} / lat :{self._lat} / lon :{self._lon}>")

    def __str__(self):
        return (f"GPSPoint<x :{self._x} / y :{self._y} / z :{self._z} / lat :{self._lat} / lon :{self._lon}>")