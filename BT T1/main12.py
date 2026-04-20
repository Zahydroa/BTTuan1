import folium

m = folium.Map(location=[10.776, 106.701], zoom_start=15)

depots = {
    'Kho_A': [10.781, 106.696],
    'Kho_B': [10.770, 106.705]
}
customers = [
    [10.783, 106.699], [10.785, 106.697], # Nhóm gần Kho A
    [10.772, 106.707], [10.768, 106.703]  # Nhóm gần Kho B
]

route_bad = [depots['Kho_A'], customers[2], customers[0], customers[3], customers[1], depots['Kho_A']]
folium.PolyLine(route_bad, color='red', weight=2, opacity=0.5, dash_array='5, 5',
                popup="Chưa tối ưu: Lộ trình chéo, tốn xăng").add_to(m)

route_opt_A = [depots['Kho_A'], customers[1], customers[0], depots['Kho_A']]
folium.PolyLine(route_opt_A, color='green', weight=5, popup="Tối ưu Xe 1 (Kho A)").add_to(m)

route_opt_B = [depots['Kho_B'], customers[3], customers[2], depots['Kho_B']]
folium.PolyLine(route_opt_B, color='blue', weight=5, popup="Tối ưu Xe 2 (Kho B)").add_to(m)

for name, pos in depots.items():
    folium.Marker(pos, popup=name, icon=folium.Icon(color='black', icon='home')).add_to(m)

for i, pos in enumerate(customers):
    folium.Marker(pos, popup=f"Khách hàng {i+1}", icon=folium.Icon(color='gray', icon='shopping-cart', prefix='fa')).add_to(m)
m.save('map.html')
import webbrowser
webbrowser.open('map.html')