import folium
import osmnx as ox
import networkx as nx

center_point = (10.776, 106.701)
G = ox.graph_from_point(center_point, dist=1000, network_type='drive')

depot_loc = (10.782, 106.705)  # Điểm Xanh (Kho)
customer_loc = (10.773, 106.697) # Điểm Cam (Khách)
orig_node = ox.nearest_nodes(G, depot_loc[1], depot_loc[0])
dest_node = ox.nearest_nodes(G, customer_loc[1], customer_loc[0])

route = nx.shortest_path(G, orig_node, dest_node, weight='length')
route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

m = folium.Map(location=center_point, zoom_start=15)

folium.PolyLine(route_coords, color='green', weight=6, opacity=0.8, popup="Driving Route").add_to(m)

folium.PolyLine([depot_loc, customer_loc], color='red', weight=2, dash_array='5, 5', opacity=0.5).add_to(m)

folium.Marker(depot_loc, icon=folium.Icon(color='blue', icon='home')).add_to(m)
folium.Marker(customer_loc, icon=folium.Icon(color='orange', icon='user')).add_to(m)
folium.Marker((10.778, 106.701), icon=folium.Icon(color='red', icon='remove-sign'), popup="Diem tac nghen").add_to(m)

title_html = '<h3 align="center" style="font-size:16px"><b>LOGISTICS DASHBOARD: Driving Route Analysis</b></h3>'
m.get_root().html.add_child(folium.Element(title_html))
m.save('map.html')
import webbrowser
webbrowser.open('map.html')