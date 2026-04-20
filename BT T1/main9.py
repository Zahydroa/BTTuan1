import pandas as pd
from sklearn.cluster import KMeans
import folium

# 1. Dữ liệu (Giữ nguyên)
data = {
    'lat': [10.7801, 10.7815, 10.7820, 10.7750, 10.7740, 10.7730, 10.7850, 10.7860, 10.7700, 10.7710],
    'lon': [106.6953, 106.6960, 106.6970, 106.7010, 106.7020, 106.7030, 106.6980, 106.6990, 106.6920, 106.6930]
}
df = pd.DataFrame(data)

# 2. Thuật toán (Quan trọng: Kiểm tra tên thuộc tính)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(df[['lat', 'lon']])

# SỬA LỖI TẠI ĐÂY: cluster_centers_ (chỉ có 1 dấu gạch dưới)
centroids = kmeans.cluster_centers_

# 3. Trực quan hóa
m = folium.Map(location=[10.778, 106.697], zoom_start=15)
colors = ['red', 'blue', 'green']

for i, center in enumerate(centroids):
    count = len(df[df['cluster'] == i])
    # Nội dung Popup: Liệt kê thuần túy
    info = f"KHO HANG CUM {i} | Phuc vu: {count} khach hang | Vai tro: Diem trung chuyen"

    folium.Marker(
        location=[center[0], center[1]],
        icon=folium.Icon(color=colors[i], icon='info-sign'),
        popup=folium.Popup(info, max_width=300)
    ).add_to(m)

# Vẽ khách hàng (Dạng chấm nhỏ cho gọn)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=3, color=colors[int(row['cluster'])], fill=True
    ).add_to(m)
m.save('map.html')
import webbrowser
webbrowser.open('map.html')