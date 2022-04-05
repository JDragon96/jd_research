"""
Copyright (c) threewaysoft. All rights reserved.
Licensed under MIT License
Author: Jaeyong Seong
"""
from ResearchLibs.base_wrapUtils import *
from ResearchLibs.base_mathUtils import *

class VectorBase:
    _x = 0
    _y = 0
    _z = 0
    _r = 0
    _g = 0
    _b = 0

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


    """ MUST BE OVERRIDE! """
    def __add__(self, other):
        raise NotImplementedError
    def __sub__(self, other):
        raise NotImplementedError
    def __truediv__(self, other):
        raise NotImplementedError
    def __repr__(self):
        raise NotImplementedError