from math import radians, cos, sin, asin, sqrt
from datetime import datetime

class GPS(object):

    def __init__(self,initLatitude,initLongtiude):
        self.name = "GPS"
        self.initLongtitude = initLongtitude
        self.initLatitude = initLatitude

    def haversine(self,lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        return km

    def velocity(self,pos1,time1,pos2,time2):
        time1 = datetime.datetime.now()
        time2 = datetime.datetime.now()
        timediff = time1-time2
        diffsecs = abs(timediff.total_seconds())
        lon1,lat1 = pos1
        lon2,lat2 = pos2
        distance_km = self.haversine(lon1, lat1, lon2, lat2)
        distance_m = distance_km*1000
        return distance_m/diffsecs


if __name__ == "__main__":
    # """
    # test code
    # """
    # initLatitude = 130
    # initLongtitude = 85
    # gps = GPS(initLatitude,initLongtitude)
    #
    # a = datetime.now()
    # b = datetime.now()
