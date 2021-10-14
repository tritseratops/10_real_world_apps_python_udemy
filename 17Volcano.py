import folium

my_map = folium.Map(location=[49.81,23.99], zoom_start=9, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes")
# markers = [[49.92,24.98],[49.72,23.88],[49.92,23.88],[49.72,24.98]]
# for coordinates in markers:
#     fg.add_child(folium.Marker(location=coordinates, popup="My Marker", icon=folium.Icon(color="green")))
# fg.add_child(folium.Marker(location=[49.82,23.98], popup="My Marker", icon=folium.Icon(color="green")))
# fg.add_child(folium.Marker(location=[49.83,23.99], popup="My Marker 2", icon=folium.Icon(color="green")))

import csv
import pandas

f_volc = pandas.read_csv("16data/Volcanoes.txt")
print(f_volc)

# f_volc = open("16data/Volcanoes.txt", "r")

# volc_data = csv.reader(f_volc)
# data_lines = list(volc_data)


# for index, row in f_volc.iterrows():
#     coordinates = [row[8],row[9]]
#     v_name = row[2]
#     v_elev = row[5]
#     v_type = row[6]
#     v_popup = v_name + " ," + str(v_elev) + " ," + v_type
#     fg.add_child(folium.Marker(location=coordinates, popup=v_popup, icon=folium.Icon(color="green")))
#     # print(volc)

v_names = list(f_volc["NAME"])
v_elevs = list(f_volc["ELEV"])
v_type = list(f_volc["TYPE"])
v_lats = list(f_volc["LAT"])
v_lons = list(f_volc["LON"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22{}%%22" target="_blank">{}</a><br>
Height: {} m <br>
Type: {}
"""

for v_name, v_elev, v_type, v_lat, v_lon in zip(v_names, v_elevs, v_type, v_lats, v_lons):
    coordinates = [v_lat, v_lon]

    iframe = folium.IFrame(html=html.format(v_name, v_name, str(v_elev), v_type), width=200, height=100)

    # color selection
    if v_elev<1000:
        v_color = "green"
    elif v_elev<2000:
        v_color = "orange"
    else:
        v_color = "red"
    # fg.add_child(folium.Marker(location=[v_lat, v_lon], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))

    # fg.add_child(folium.Marker(location=coordinates, popup=folium.Popup(iframe), icon=folium.Icon(color=v_color)))
    fg.add_child(folium.CircleMarker(location=coordinates, radius = 6, popup=folium.Popup(iframe),
                                     color = v_color, fill_color = v_color, fill=True,
                                     fill_opacity=0.7))




# add countries
countries_data = open("16data/world.json", "r", encoding='utf-8-sig').read()

fg_density = folium.FeatureGroup(name="Countries Density")

def country_color(country_json):
    area  = country_json['properties']['AREA']
    pop = country_json['properties']['POP2005']
    density = (pop/area) if area !=0 else 0
    # if pop<1000000:
    #     return 'green'
    # elif pop<100000000:
    #     return 'orange'
    # else:
    #     return 'red'
    if density<25:
        return 'blue'
    elif density < 50:
        return 'green'
    elif density<100:
        return 'yellow'
    elif density<200:
        return 'orange'
    elif density<400:
        return 'red'
    elif density<800:
        return 'crimson'
    else:
        return 'black'


fg_density.add_child(folium.GeoJson(data=countries_data, style_function = lambda x: {'fillColor':country_color(x), 'fillOpacity':'0.7'}))
my_map.add_child(fg_density)
my_map.add_child(fg)

# my_map.add_child(folium.GeoJson(data=countries_data, style_function = lambda x: {'fillColor':country_color(x), 'fillOpacity':'0.7'}))\
# my_map.add_child(fg, name="Density")



my_map.add_child(folium.LayerControl())


my_map.save("Map1.html")
# dir(my_map)

# tiles = "Mapbox Bright"
#
# Please use this instead:
#
# tiles = "Stamen Terrain"

