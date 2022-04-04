from ResearchLibs.DataStructure.Vector2D import Vector2D
from ResearchLibs.DataStructure.GPS import GPSPoint

def GPS2Vector2D(gps):
    return Vector2D(gps._x, gps._y, gps._z)

def Vector2GPS(vector):
    return GPSPoint(vector.x, vector.y, vector.z)