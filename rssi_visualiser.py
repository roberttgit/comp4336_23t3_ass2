import folium
import folium.plugins
import pandas as pd

map_centre = [-33.91757, 151.22906]

df = pd.read_csv("dataset.csv")

#only rows with latency (i.e: connected to uniwide)
df = df.dropna(subset=["network delay (ms)"], inplace=False)

#unique only
df = df.drop_duplicates(subset=["gps latitude", "gps longitude"], keep='first')

# convert from dbm to percentage
df["rssi"] = df["rssi"].apply(lambda x: 2*(x+100))


#get required cols only
dps = df[["gps latitude", "gps longitude", "rssi"]]

print(dps)
m1 = folium.Map(location=map_centre, zoom_start = 19, control_scale=True)
# for index, record in dps.iterrows():
#     #print(record)
#     folium.Marker([record['gps latitude'], record['gps longitude']]).add_to(m)


hm1 = folium.plugins.HeatMap(dps, radius=34)
hm1.add_to(m1)

m1.save("maps/uniwide_rssi.html")

#add the new waps
m2 = m1
new_wap_df = pd.read_csv("addwap_gps.csv")
new_wap_df["rssi"] = new_wap_df["rssi"].apply(lambda x: 2*(x+100))
print(df)
print("\n")
print(new_wap_df)
df2 = df._append(new_wap_df)

dps2 = df2[["gps latitude", "gps longitude", "rssi"]]
print(dps2)
hm2 = folium.plugins.HeatMap(dps2, radius=34)
hm2.add_to(m2)

m2.save("maps/uniwide_upgrade_rssi.html")