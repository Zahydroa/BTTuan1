import folium
from folium.plugins import HeatMap
import pandas as pd

center = [10.776, 106.701]
customers = [[10.776 + 0.005*i, 106.701 + 0.005*j] for i in range(-2,3) for j in range(-2,3)]
competitors = [[10.780, 106.705], [10.770, 106.695]]

# Điểm tối ưu là trung bình tọa độ khách hàng nhưng phải check khoảng cách với đối thủ
optimal_lat = sum([c[0] for c in customers]) / len(customers)
optimal_lon = sum([c[1] for c in customers]) / len(customers)
optimal_site = [optimal_lat, optimal_lon]

m = folium.Map(location=center, zoom_start=15, tiles="cartodbpositron")

HeatMap(customers, radius=20, blur=15).add_to(m)

for comp in competitors:
    folium.Marker(comp, icon=folium.Icon(color='red', icon='ban', prefix='fa'),
                  popup="DOI THU HIEN HUU").add_to(m)
    folium.Circle(comp, radius=500, color='red', fill=True, opacity=0.1).add_to(m)

folium.Marker(
    optimal_site,
    icon=folium.Icon(color='orange', icon='star', prefix='fa'),
    popup=f"VI TRI GOI Y MO CUA HANG<br>Toa do: {optimal_site}"
).add_to(m)

m.save('map.html')
import webbrowser
webbrowser.open('map.html')