from ResearchLibs.DataStructure.DataConverter import *
from ResearchLibs.base_mathUtils import *
from ResearchLibs.GISLib.GIS_GPS_Calculator import GPS_Calculator

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

    # 2. 기준 GPS값과 타겟 포인트 사이의 bearing 계산
    t = Vector2D(-10, 10, 11.599462)
    p0 = GPS2Vector2D(g0)
    p1 = GPS2Vector2D(g1)

    base_vector = p1 - p0
    target_vector = t - p0
    target_bearing_deg = VectorMATH.vec_clockwise_angle(base_vector, target_vector)

    # 3. 자오선에 대한 target의 bearing 계산
    total_bearing = target_bearing_deg + base_bearing_deg
    
    # 4. g0에 대한 target 사이의 거리 계산(km)
    base_distance = GPS_Calculator.HarverSine(g0, g1)
    base_point_distance = p0.vector_distance_2D(p1)
    ratio = base_distance / base_point_distance
    print(base_distance, base_point_distance)
    distance = p0.vector_distance_2D(t) * 0.001 * ratio
    new_gps = GPS_Calculator.GPS_Bearing(g0, distance, total_bearing)

    print(distance)
    print(new_gps)


GPS_Mapping_Pipeline()

# 34.33253970670793, 134.04812746994347
# 34.33249964647181, 134.04854603405