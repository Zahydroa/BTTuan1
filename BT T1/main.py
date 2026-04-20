
import folium

map = folium.Map(location=[10.7626, 106.6602], zoom_start=13)

places = [
    ("UEH", 10.76112744881392, 106.668365544879),
    ("Cafe", 10.761182812295305, 106.66464568209057),
    ("Mall", 10.770644886828839, 106.67044385140066),
    ("Park", 10.757331582147291, 106.66708755360338),
    ("Library", 10.757726955394704, 106.66900045520683),
]

for name, lat, lon in places:
    folium.Marker([lat, lon], popup=name).add_to(map)

map.save("23_1.html")
import webbrowser
webbrowser.open("23_1.html")