import folium
import networkx as nx
import osmnx as ox

center = (10.7801, 106.6953)
G = ox.graph_from_point(center, dist=800, network_type='drive')
nodes_list = list(G.nodes)
orig, dest = nodes_list[0], nodes_list[-1]

path_dijkstra = nx.shortest_path(G, source=orig, target=dest, weight='length', method='dijkstra')
path_astar = nx.astar_path(G, source=orig, target=dest, weight='length')

m = folium.Map(location=center, zoom_start=16)

coords_dijkstra = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path_dijkstra]
folium.PolyLine(
    coords_dijkstra, color='blue', weight=8, opacity=0.4,
    popup=f"Số node duyệt: {len(path_dijkstra)} & Đặc điểm: Quét diện rộng, chính xác 100%."
).add_to(m)

coords_astar = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path_astar]
folium.PolyLine(
    coords_astar, color='red', weight=3, opacity=1,
    popup=f"Số node duyệt: {len(path_astar)} & Đặc điểm: Có hướng đích, nhanh, tiết kiệm tài nguyên."
).add_to(m)

folium.Marker([G.nodes[orig]['y'], G.nodes[orig]['x']], popup="Start", icon=folium.Icon(color='gray')).add_to(m)
folium.Marker([G.nodes[dest]['y'], G.nodes[dest]['x']], popup="End", icon=folium.Icon(color='black')).add_to(m)

m.save('map.html')
import webbrowser
webbrowser.open('map.html')