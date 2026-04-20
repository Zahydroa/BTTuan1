import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np

data = {
    'lat': [10.780, 10.781, 10.782, 10.772, 10.773, 10.774, 10.760, 10.762],
    'lon': [106.695, 106.696, 106.697, 106.700, 106.701, 106.702, 106.680, 106.682],
    'demand_score': [90, 85, 95, 40, 45, 35, 10, 15] # Nhu cầu từ 0-100
}
df = pd.DataFrame(data)

threshold = 50
df['priority'] = df['demand_score'].apply(lambda x: 'CAO' if x > threshold else 'THAP')

m = folium.Map(location=[10.775, 106.695], zoom_start=14)

heat_data = [[row['lat'], row['lon'], row['demand_score']] for index, row in df.iterrows()]
HeatMap(heat_data, radius=25, blur=15, gradient={0.4: 'blue', 0.65: 'yellow', 1: 'red'}).add_to(m)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=5,
        color='black',
        popup=f"Nhu cau: {row['demand_score']} | Uu tien: {row['priority']}"
    ).add_to(m)

m.save('map.html')
import webbrowser
webbrowser.open('map.html')

print("TONG HOP DIEU PHOI NGUON LUC:")
print(df['priority'].value_counts())