import folium
import folium.plugins
import pandas as pd

map_centre = [-33.91757, 151.22906]
latency_threshold = 40

# Read the CSV file into a DataFrame
df = pd.read_csv('dataset.csv')

#ignore weak rssi
df = df[df['network delay (ms)'] > latency_threshold]

dps = df[["gps latitude", "gps longitude", "network delay (ms)"]]

m = folium.Map(location=map_centre, zoom_start = 19, control_scale=True)
hm = folium.plugins.HeatMap(dps)
hm.add_to(m)

m.save("maps/latency.html")