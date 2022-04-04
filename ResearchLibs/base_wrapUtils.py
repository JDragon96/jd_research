"""
Copyright (c) threewaysoft. All rights reserved.
Licensed under MIT License
Author: Jaeyong Seong
"""
import numpy as np

def nparray_wrapping_func(func):
    def wrap_function(param):
        param = np.array(param)
        return func(param)
    return wrap_function

def nparray_wrapping_func_two(func):
    def wrap_function(v1, v2):
        v1 = np.array(v1)
        v2 = np.array(v2)
        return func(v1, v2)
    return wrap_function