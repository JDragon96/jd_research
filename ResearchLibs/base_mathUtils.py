"""
Copyright (c) threewaysoft. All rights reserved.
Licensed under MIT License
Author: Jaeyong Seong
"""
from ResearchLibs.DataStructure.Vector2D import *
import math

class CircularMATH:

    @staticmethod
    def rad2deg(rad):
        return rad / np.pi * 180

    @staticmethod
    def deg2rad(deg):
        return deg / 180 * np.pi

class VectorMATH:
    @staticmethod
    def vec_cross_product(vec0, vec1, check=False):
        result = [vec0._y * vec1._z - vec0._z * vec1._y,
                  vec0._z * vec1._x - vec0._x * vec1._z,
                  vec0._x * vec1._y - vec0._y * vec1._x]
        print(f"result : {result}")
        if check:
            if result[2] > 0:
                return True
            return False

        return result

    @staticmethod
    def vec_clockwise_angle(vec0, vec1):
        flip = VectorMATH.vec_cross_product(vec0, vec1, True)
        dot_cos = vec0.vector_dot(vec1) / (vec0.vector_abs() * vec1.vector_abs())
        dot_deg = CircularMATH.rad2deg(math.acos(dot_cos))

        if flip:
            return 360 - dot_deg
        else:
            return dot_deg


@nparray_wrapping_func
def vector_absolute(v):
    return pow(pow(v[0], 2) + pow(v[1], 2), 0.5)

@nparray_wrapping_func
def vector_normalization(v):
    vector_abs = vector_absolute(v)
    return np.array([v[0] / vector_abs, v[1] / vector_abs])

@nparray_wrapping_func_two
def genNewVector(v1, v2):
    return np.array([v2[0] - v1[0], v2[1] - v1[1]])

def vector_normalization_two(v1, v2):
    new_vector = genNewVector(v1, v2)
    vector_abs = vector_absolute(new_vector)
    return np.array([new_vector[0] / vector_abs, new_vector[1] / vector_abs])