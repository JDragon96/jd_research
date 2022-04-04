"""
Copyright (c) threewaysoft. All rights reserved.
Licensed under MIT License
Author: Jaeyong Seong
"""
from ResearchLibs.base_DataStructure import *
from ResearchLibs.base_mathUtils import *
from ResearchLibs.base_wrapUtils import *

class Vector2D(VectorBase):
    def vector_norm2D(self):
        abs_v = pow(pow(self._x, 2) + pow(self._y, 2), 0.5)
        # self._x = self._x / abs_v
        # self._y = self._y / abs_v
        # return self
        return Vector2D(self._x / abs_v, self._y / abs_v)

    def vector_rotation2D(self, angle: float):
        rad = CircularMATH.deg2rad(abs(angle))
        if angle > 0:
            """ 반시계방향 회전 """
            x = self._x * np.cos(rad) - self._y * np.sin(rad)
            y = self._x * np.sin(rad) + self._y * np.cos(rad)
            return Vector2D(x, y)
        elif angle < 0:
            """ 시계방향 회전 """
            x = self._x * np.cos(rad) + self._y * np.sin(rad)
            y = -self._x * np.sin(rad) + self._y * np.cos(rad)
            return Vector2D(x, y)
        else:
            return self

    def vector_slope_deg_2D(self):
        return round(CircularMATH.rad2deg(np.arctan(self._y / self._x)), 2)

    def vector_distance_2D(self, other):
        return pow(pow(self._x - other._x, 2) + pow(self._y - other._y, 2), 0.5)

    def vector_abs(self):
        return pow(pow(self._x, 2) + pow(self._y, 2), 0.5)

    def vector_cross(self, other):
        return self._x * other._y - self._y * other._x

    def vector_dot(self, other):
        return self._x * other._x + self._y * other._y


    """ MAGIC METHODS! """
    def __add__(self, other):
        return Vector2D(self._x + other._x, self._y + other._y, self._z + other._z)
    def __sub__(self, other):
        return Vector2D(self._x - other._x, self._y - other._y, self._z - other._z)
    def __truediv__(self, other):
        if other == 0:
            raise NotImplementedError("[Vector2D] ZERO DIVISION ERROR...")
        return Vector2D(self._x/other, self._y/other, self._z/other)
    def __mul__(self, other):
        return Vector2D(self._x * other, self._y * other, self._z * other)
    def __repr__(self):
        return f"Vector2D<{self._x}, {self._y}>"



class Point2D(VectorBase):
    """ MAGIC METHODS! """
    def __add__(self, other):
        return Vector2D(self._x + other._x, self._y + other._y, self._z + other._z)
    def __sub__(self, other):
        return Vector2D(self._x - other._x, self._y - other._y, self._z - other._z)
    def __truediv__(self, other):
        if other == 0:
            raise NotImplementedError("[Point2D] ZERO DIVISION ERROR...")
        return Vector2D(self._x/other, self._y/other, self._z/other)
    def __mul__(self, other):
        return Vector2D(self._x * other, self._y * other, self._z * other)
    def __repr__(self):
        return f"Point2D<{self._x}, {self._y}>"


""" Wrapping Method! """
@nparray_wrapping_func
def array2Vector2D(ary):
    """ (N, 3) 배열을 Vector 배열로 전환 """
    points = []

    if len(ary.shape) > 1:
        if ary.shape[1] != 3:
            ary = ary.T
        for v in ary:
            points.append(Vector2D(v[0], v[1], v[2]))
        return points
    else:
        return Vector2D(ary[0], ary[1], ary[2])

@nparray_wrapping_func
def array2Point2D(ary):
    """ (N, 3) 배열을 Vector 배열로 전환 """
    points = []

    if len(ary.shape) > 1:
        if ary.shape[1] != 3:
            ary = ary.T
        for p in ary:
            points.append(Point2D(p[0], p[1]))
        return points
    else:
        return Point2D(ary[0], ary[1])

def Vector2array(vectors):
    new_array = []
    for v in vectors:
        new_array.append([v._x, v._y, v._z])
    return np.array(new_array)