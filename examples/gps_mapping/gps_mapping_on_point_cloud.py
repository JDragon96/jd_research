from ResearchLibs.GISLib.GIS_GPS_Calculator import GPS_Calculator
from ResearchLibs.GISLib.GPS_Manager import GPSManager
from ResearchLibs.base_mathUtils import *
from ResearchLibs.DataStructure.DataHandler import *
from ResearchLibs.IOLib.File_Handler import getOnlyFileName
from ResearchLibs.DataStructure.GPS import GPSPoint
import copy
import json

def DataCrop(data, target_gps):
    crop_data = []
    for d in data:
        if GPS_Calculator.HarverSine_v2(d[0], d[1], target_gps._lat, target_gps._lon) < 2:
            crop_data.append(d)

    return crop_data


def GPS_MAPPING_ON_POINT_CLOUD_PIPELINE(gpsfile, datafile, debug=False):
    ## 0. load data
    hub = DATA_HUB(datafile, getOnlyFileName(datafile), debug)
    data = hub.DATA_load()

    ## 1. gps sort
    manager = GPSManager(gpsfile)
    manager.Manager_Setting_Pipeline(debug)

    x = []
    y = []
    z = []
    r = []
    g = []
    b = []
    # data = [Vector2D(-10, 0, 0)]

    for t in data:
        ## 2. calculate target point's bearing
        target_vector = t - manager.getGPS_Point0()
        target_bearing_deg = VectorMATH.vec_clockwise_angle(manager.getBaseVector(), target_vector)
        total_bearing = target_bearing_deg + manager.getBearing()

        ## 3. calculate distance between target and gps0
        distance = manager.getGPS_Point0().vector_distance_2D(t) * 0.001

        if total_bearing > 360:
            total_bearing -= 360

        ## 4. calculate new gps point using distance and bearing!
        new_gps = manager.getNewGPS_Using_Bearing_and_Distance(distance, total_bearing)

        ## 5. 데이터 추가
        x.append(new_gps._lat)
        y.append(new_gps._lon)
        z.append(t._z)
        r.append(t._r)
        g.append(t._g)
        b.append(t._b)

    ## GPS => POINT CLOUD(METER) SCALING
    save_data = np.vstack([x, y, z, r, g, b])
    save_data[0] *= -manager.lat_scaling()     # inverse x-axis
    save_data[1] *= manager.lon_scaling()
    min_x = min(save_data[0])
    min_y = min(save_data[1])
    save_data[0] -= min_x
    save_data[1] -= min_y

    json_data = {
        "gps_file": gpsfile,
        "data_file": datafile,
        "lat_scale": manager.lat_scaling(),
        "lon_scale": manager.lon_scaling(),
        "min_x": min_x,
        "min_y": min_y
    }

    ## las save
    hub.DATA_save(save_data)

    ## META DATA SAVE
    with open(f".\\{getOnlyFileName(datafile)}.json", "w") as json_file:
        json.dump(json_data, json_file)

if __name__=="__main__":
    GPS_MAPPING_ON_POINT_CLOUD_PIPELINE("test_data.txt", r"E:\test_data.las", True)