from shapely.geometry import shape, Point
import json
# depending on your version, use: from shapely.geometry import shape, Point

# load GeoJSON file containing sectors
with open('sfpd_districts2.json') as f:
    js = json.load(f)

# construct point based on lon/lat returned by geocoder
point = Point(-122.4363949, 37.7939175)
print(point)
# check each polygon to see if it contains the point
for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print(feature['properties']['DISTRICT'])
