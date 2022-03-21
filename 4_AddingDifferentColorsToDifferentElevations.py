import folium
import pandas

#In this code we added new function color_producer and also replaced Marker with CircleMarker

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map')

for lt,ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + ' meters',
    fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))
    #icon = folium.Icon(color = color_producer(el))))

map.add_child(fg)

map.save('4_AddingDifferentColorsToDifferentElevations.html')
