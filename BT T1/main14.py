import folium
from folium.plugins import TimestampedGeoJson
import osmnx as ox
import networkx as nx

center = (10.776, 106.701)
G = ox.graph_from_point(center, dist=800, network_type='drive')

depot = (10.782, 106.705)
customer = (10.773, 106.697)
orig = ox.nearest_nodes(G, depot[1], depot[0])
dest = ox.nearest_nodes(G, customer[1], customer[0])
route = nx.shortest_path(G, orig, dest, weight='length')
route_coords = [[G.nodes[n]['x'], G.nodes[n]['y']] for n in route] # Lưu ý: [Lon, Lat] cho GeoJSON

features = []
for i, coord in enumerate(route_coords):
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': coord,
        },
        'properties': {
            'time': f'2026-04-20T11:{i:02d}:00', 
            'popup': f'Xe dang o vi tri {i}',
            'icon': 'marker',
            'iconstyle': {
                'iconUrl': 'https://cdn-icons-png.flaticon.com/512/3448/3448339.png',
                'iconSize': [30, 30]
            }
        }
    }
    features.append(feature)

m = folium.Map(location=center, zoom_start=15)

folium.PolyLine([(c[1], c[0]) for c in route_coords], color='gray', weight=2, opacity=0.5).add_to(m)

TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': features},
    period='PT1M', 
    add_last_point=True,
    auto_play=True,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options='HH:mm',
    time_slider_drag_update=True
).add_to(m)
m.save('map.html')
import webbrowser
webbrowser.open('map.html')