import folium
from folium.plugins import HeatMap
import numpy as np

center_coords = [10.7769, 106.7009]
m = folium.Map(location=center_coords, zoom_start=14, tiles="cartodbpositron")

np.random.seed(42)
data = (np.random.normal(size=(50, 2)) * 0.01 + np.array(center_coords)).tolist()

def get_admin_info(val):
    if val > 0.8:
        return "Đỏ (Nóng)", " TRỌNG ĐIỂM: Cần mở thêm chi nhánh và tăng shipper ngay lập tức."
    elif val > 0.5:
        return "Cam (Ấm)", " TIỀM NĂNG: Phù hợp để chạy quảng cáo khuyến mãi kích cầu."
    else:
        return "Xanh (Lạnh)", " VÙNG TRỐNG: Cần nghiên cứu đối thủ hoặc gom đơn để giảm chi phí."

heat_data = []
for point in data:
    intensity = np.random.rand() 
    heat_data.append([point[0], point[1], intensity])

    label, desc = get_admin_info(intensity)

    folium.CircleMarker(
        location=[point[0], point[1]],
        radius=15, 
        color=None,
        fill=True,
        fill_color=None,
        fill_opacity=0, 
        popup=folium.Popup(f"<b>Vùng {label}</b><br>{desc}", max_width=250),
        tooltip="Click để xem ý nghĩa quản trị"
    ).add_to(m)

HeatMap(heat_data, radius=25, blur=15, min_opacity=0.5).add_to(m)

legend_html = """
<div style="position: fixed; bottom: 50px; left: 50px; width: 200px; z-index:9999;
            background-color:white; border:2px solid grey; padding: 10px; border-radius: 10px;">
    <b>HƯỚNG DẪN:</b><br>
    Click vào các điểm màu trên bản đồ để xem phân tích quản trị.<br>
    🔴: Nóng | 🟠: Tiềm năng | 🔵: Lạnh
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file and open it in the default browser
m.save('map.html')
import webbrowser
webbrowser.open('map.html')