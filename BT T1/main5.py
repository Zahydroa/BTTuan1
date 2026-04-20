import folium

warehouse_coords = [10.7715, 106.6685]

m = folium.Map(location=warehouse_coords, zoom_start=13)

service_zones = [
    {"radius": 10000, "color": "green", "label": "Vùng 10km (Tiếp cận thấp)", "opacity": 0.1},
    {"radius": 5000, "color": "orange", "label": "Vùng 5km (Tiếp cận trung bình)", "opacity": 0.2},
    {"radius": 3000, "color": "red", "label": "Vùng 3km (Tiếp cận cao - Giao nhanh)", "opacity": 0.3}
]

for zone in service_zones:
    folium.Circle(
        location=warehouse_coords,
        radius=zone["radius"],
        color=zone["color"],
        fill=True,
        fill_color=zone["color"],
        fill_opacity=zone["opacity"],
        popup=zone["label"]
    ).add_to(m)

folium.Marker(
    location=warehouse_coords,
    popup="<b>TRUNG TÂM PHÂN PHỐI TỔNG</b>",
    icon=folium.Icon(color='black', icon='truck', prefix='fa')
).add_to(m)

customers = [
    {"name": "Khách A", "coords": [10.7850, 106.6850], "status": "Trong vùng 3km"},
    {"name": "Khách B", "coords": [10.8100, 106.7000], "status": "Trong vùng 5km"},
    {"name": "Khách C", "coords": [10.8500, 106.6500], "status": "Ngoài vùng giao nhanh"}
]

for cust in customers:
    folium.Marker(
        location=cust["coords"],
        popup=f"{cust['name']}: {cust['status']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)
m.save('map.html')
import webbrowser
webbrowser.open('map.html')