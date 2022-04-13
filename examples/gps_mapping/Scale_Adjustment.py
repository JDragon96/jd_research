from ResearchLibs.DataStructure.Vector2D import Vector2D
import json

def Meter2GPS(vec):
    with open("test_data.json", "r") as st_json:
        meta = json.load(st_json)

    base_vec = Vector2D(meta["min_x"], meta["min_y"], 0)
    new_vec = vec + base_vec
    new_vec._x /= -meta["lat_scale"]
    new_vec._y /= meta["lon_scale"]

    print(new_vec)

# 0 ~ 5m 오차 발생(안드로이드 GPS 활용 시)
# 정밀 GPS를 사용 할 수록 정학도는 올라감..
# Meter2GPS(Vector2D(76.589600, 120.631332, 0))
# Meter2GPS(Vector2D(54.079430, 54.007717, 0))
Meter2GPS(Vector2D(14.280293, 80.292130, 0))