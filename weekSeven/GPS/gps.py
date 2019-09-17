# @Author: subalakshmi
# @Date:   2019-09-16T11:23:53+05:30
# @Last modified by:   subalakshmi
# @Last modified time: 2019-09-17T11:27:47+05:30

import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv','r') as fileHandler:
    reader=csv.reader(fileHandler)
    k = 0
    for row in reader:
        latitute = float(row[0])
        longitude = float(row[1])
        #print(str(latitute)+','+str(longitude))
        if(k==0):
            gmap.marker(latitute,longitude,'yellow')
            k = 1
        else:
            gmap.marker(latitute,longitude,'blue')
gmap.marker(latitute,longitude,'red')
#Add Gmap apikey - get your own and set it as gmap.apikey="Your API KEY"
# Also make sure that you enable JavaScript API support for Google Maps.
# Place map - for golden lake park
gmap.draw("goldenlakeplot.html")
# GoogleMapPlotter - lat long and zoom resolution
