import folium

map_center = [10.8015, 106.7115]
m = folium.Map(location=map_center, zoom_start=16)

roads = [
    {"name": "Xo Viet Nghe Tinh", "coords": [[10.800, 106.711], [10.803, 106.712]], "flow": 95},
    {"name": "Dien Bien Phu", "coords": [[10.801, 106.708], [10.802, 106.715]], "flow": 65},
    {"name": "Bach Dang", "coords": [[10.803, 106.710], [10.805, 106.708]], "flow": 30}
]

for road in roads:
    if road['flow'] > 80:
        color = 'red'
        risk = "CAO (Tac nghen)"
    elif road['flow'] > 50:
        color = 'orange'
        risk = "TRUNG BINH (Mat do cao)"
    else:
        color = 'green'
        risk = "THAP (Thong thoang)"

    folium.PolyLine(
        road['coords'],
        color=color,
        weight=8,
        opacity=0.8,
        popup=f"Duong: {road['name']} | Nguy co: {risk}"
    ).add_to(m)

alt_route = [[10.800, 106.711], [10.799, 106.713], [10.802, 106.715]]
folium.PolyLine(
    alt_route,
    color='darkgreen',
    weight=5,
    dash_array='10, 10',
    popup="TUYEN DUONG THAY THE DE XUAT"
).add_to(m)

folium.Marker(
    [10.8015, 106.7115],
    icon=folium.Icon(color='red', icon='warning', prefix='fa'),
    popup="CANH BAO: Diem den tac nghen"
).add_to(m)
m.save('map.html')
import webbrowser
webbrowser.open('map.html')