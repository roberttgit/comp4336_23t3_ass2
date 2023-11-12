import folium
import folium.plugins
import pandas as pd

map_centre = [-33.91757, 151.22906]

df = pd.read_csv("addwap_gps.csv")

#get required cols only
dps = df[["gps latitude", "gps longitude"]]

print(dps)
m = folium.Map(location=map_centre, zoom_start = 19, control_scale=True)
for index, record in dps.iterrows():
    #print(record)
    folium.Marker([record['gps latitude'], record['gps longitude']]).add_to(m)


m.save("maps/addwap_locs.html")
