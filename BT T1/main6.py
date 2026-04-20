import folium
import osmnx as ox

# 1. Định nghĩa 3 khu vực trọng điểm để làm Walking Route
# Chúng ta chọn 3 điểm có đặc điểm hạ tầng khác nhau để so sánh
locations = [
    {"name": "Khu vực Hồ Con Rùa", "coords": (10.7827, 106.6958), "color": "purple"},
    {"name": "Khu vực Chợ Bến Thành", "coords": (10.7725, 106.6980), "color": "orange"},
    {"name": "Khu vực Phố đi bộ Nguyễn Huệ", "coords": (10.7741, 106.7038), "color": "blue"}
]

# 2. Khởi tạo bản đồ trung tâm Quận 1
m = folium.Map(location=[10.778, 106.699], zoom_start=15, tiles="cartodbpositron")

# 3. Lặp qua từng địa điểm để tải mạng lưới đi bộ và tính toán thông số
for loc in locations:
    try:
        # Tải mạng lưới đi bộ bán kính 300m (nhỏ để chạy nhanh, không lỗi server)
        G = ox.graph_from_point(loc['coords'], dist=300, network_type='walk')

        # Tính toán các thông số theo yêu cầu đề bài
        stats = ox.basic_stats(G)
        num_nodes = stats['n']
        avg_length = stats['edge_length_avg']
        # Mật độ = Tổng chiều dài (km) / Diện tích (giả định diện tích quét ~0.28 km2)
        density = (stats['edge_length_total'] / 1000) / 0.28

        # Tạo nội dung Popup "Show off" thông số quản trị
        popup_html = f"""
        <div style="width: 200px; font-family: sans-serif;">
            <h4 style="color:{loc['color']}; margin-bottom:5px;">{loc['name']}</h4>
            <hr style="margin:5px 0;">
            <b>👣 Thông số Walking Route:</b><br>
            • Số nút giao: <b>{num_nodes}</b><br>
            • Chiều dài TB đoạn: <b>{avg_length:.1f} m</b><br>
            • Mật độ mạng: <b>{density:.2f} km/km²</b>
        </div>
        """

        # Chuyển đổi sang GeoDataFrame để vẽ các con đường thực tế (Walking routes)
        gdf_edges = ox.graph_to_gdfs(G, nodes=False)

        # Vẽ từng đoạn đường thực tế lên bản đồ
        for _, row in gdf_edges.iterrows():
            sim_geo = row['geometry']
            if sim_geo.geom_type == 'LineString':
                path_coords = [(lat, lon) for lon, lat in sim_geo.coords]
                folium.PolyLine(
                    locations=path_coords,
                    color=loc['color'],
                    weight=4,
                    opacity=0.7,
                    popup=folium.Popup(popup_html, max_width=250),
                    tooltip=f"Click xem thông số {loc['name']}"
                ).add_to(m)

        # Thêm Marker tại tâm điểm khu vực
        folium.Marker(
            loc['coords'],
            icon=folium.Icon(color=loc['color'], icon='info-sign')
        ).add_to(m)

    except Exception as e:
        print(f"Lỗi khi tải khu vực {loc['name']}: {e}")

m.save('map.html')
import webbrowser
webbrowser.open('map.html')