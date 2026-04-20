import folium
from geopy.distance import geodesic

customer_loc = [10.7801, 106.6953] 
drivers = [
    {"id": "Bike_Fast", "coords": [10.7830, 106.6980], "type": "Motorbike", "speed_kmh": 30},
    {"id": "Car_Slow", "coords": [10.7750, 106.6910], "type": "Car", "speed_kmh": 15}, 
    {"id": "Bike_Distance", "coords": [10.7950, 106.7050], "type": "Motorbike", "speed_kmh": 40}
]

for d in drivers:
    d['dist'] = geodesic(customer_loc, d['coords']).km
    d['eta'] = (d['dist'] / d['speed_kmh']) * 60 

best_driver = min(drivers, key=lambda d: d['eta'])

m = folium.Map(location=customer_loc, zoom_start=15, tiles="cartodbpositron")

folium.Marker(customer_loc, icon=folium.Icon(color='red', icon='street-view', prefix='fa')).add_to(m)

for d in drivers:
    is_best = (d == best_driver)
    color = 'green' if is_best else 'red' if d['speed_kmh'] < 20 else 'gray'

    folium.Marker(
        d['coords'],
        icon=folium.Icon(color=color, icon='motorcycle' if d['type']=='Motorbike' else 'car', prefix='fa'),
        popup=f"ID: {d['id']}; Thời gia di chuyển: {d['eta']:.1f} phút"
    ).add_to(m)

    folium.PolyLine(
        [customer_loc, d['coords']],
        color=color,
        weight=5 if is_best else 2,
        opacity=0.8 if is_best else 0.3,
        popup=folium.Popup(f"""

                PHÂN TÍCH ĐIỀU VẬN
                 Khoảng cách: {d['dist']:.2f} km<br>
                 Vận tốc TB: {d['speed_kmh']} km/h<br>
                 Thời gian di chuyển: {d['eta']:.1f} phút</b><br>
                 Kết luận: {'NÊN GÁN' if is_best else 'KHÔNG TỐI ƯU'}
            </div>
        """, max_width=250)
    ).add_to(m)

m.save('map.html')
import webbrowser
webbrowser.open('map.html')