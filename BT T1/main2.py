#BÀI 2
import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

geolocator = Nominatim(user_agent="ueh_test_app", timeout=10)


center_addr = "Đại học Kinh tế, Quận 3, Hồ Chí Minh"
loc_center = geolocator.geocode(center_addr)


if loc_center:
    latlng_center = (loc_center.latitude, loc_center.longitude)
    print(f"Đã tìm thấy tọa độ trung tâm: {latlng_center}")
else:
    
    latlng_center = (10.7801, 106.6953)
    print("sử dụng tọa độ mặc định.")


addresses = [
    "Dinh Độc Lập", "Chợ Bến Thành", "Nhà thờ Đức Bà",
    "Bitexco Tower", "Landmark 81", "Bệnh viện Từ Dũ",
    "Thảo Cầm Viên", "Hồ Con Rùa", "Bưu điện Thành phố", "Bảo tàng Mỹ thuật"
]


m = folium.Map(location=latlng_center, zoom_start=14, control_scale=True)
folium.Marker(latlng_center, popup="TRUNG TÂM (UEH)", icon=folium.Icon(color='red')).add_to(m)


for addr in addresses:
    try:
        time.sleep(1)
        location = geolocator.geocode(f"{addr}, Hồ Chí Minh")

        if location:
            latlng_dest = (location.latitude, location.longitude)
            dist = geodesic(latlng_center, latlng_dest).km

            folium.Marker(latlng_dest, popup=f"{addr}: {dist:.2f} km").add_to(m)
            folium.PolyLine([latlng_center, latlng_dest], color='blue', weight=1, opacity=0.5).add_to(m)
            print(f"{addr}: {dist:.2f} km")
        else:
            print(f"Không tìm thấy tọa độ cho: {addr}")

    except Exception as e:
        print(f"Lỗi kết nối khi tìm {addr}: {e}")

m