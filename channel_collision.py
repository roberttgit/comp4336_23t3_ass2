import folium
import folium.plugins
import pandas as pd

map_centre = [-33.91757, 151.22906]

# Read the CSV file into a DataFrame
df = pd.read_csv('dataset.csv')

#ignore weak rssi
df = df[df['rssi'] > -70]

# Group the data by GPS coordinates and channel
grouped = df.groupby(['gps latitude', 'gps longitude', 'channel'])

# Count the occurrences of each combination
occurrences = grouped.size().reset_index(name='Collision Count')

# Filter locations with a high occurrence of channel collisions
threshold = 3  # You can adjust this threshold as needed
high_collision_locations = occurrences[occurrences['Collision Count'] >= threshold]

# Print or save the report
high_collision_locations.to_csv('high_collision_locations.csv', index=False)
print(high_collision_locations)


m = folium.Map(location=map_centre, zoom_start = 19, control_scale=True)
# for index, record in dps.iterrows():
#     #print(record)
#     folium.Marker([record['gps latitude'], record['gps longitude']]).add_to(m)

dps = high_collision_locations[["gps latitude", "gps longitude", "Collision Count"]]
hm = folium.plugins.HeatMap(dps)
hm.add_to(m)

m.save("maps/channel_collisions.html")