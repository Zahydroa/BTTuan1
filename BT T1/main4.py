import folium
import pandas as pd
import json

hcm_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "Quận 1"},
            "geometry": {"type": "Polygon", "coordinates": [[[106.69, 10.77], [106.70, 10.77], [106.70, 10.78], [106.69, 10.78], [106.69, 10.77]]]}
        },
        {
            "type": "Feature",
            "properties": {"name": "Quận 3"},
            "geometry": {"type": "Polygon", "coordinates": [[[106.67, 10.77], [106.68, 10.77], [106.68, 10.78], [106.67, 10.78], [106.67, 10.77]]]}
        },
        {
            "type": "Feature",
            "properties": {"name": "Quận 10"},
            "geometry": {"type": "Polygon", "coordinates": [[[106.66, 10.76], [106.67, 10.76], [106.67, 10.77], [106.66, 10.77], [106.66, 10.76]]]}
        }
    ]
}
data = pd.DataFrame({
    'District': ['Quận 1', 'Quận 3', 'Quận 10'],
    'Value': [95, 70, 45]  # Doanh thu hoặc mật độ tiêu thụ
})

m = folium.Map(location=[10.7769, 106.68], zoom_start=14)

folium.Choropleth(
    geo_data=hcm_geojson,      
    name="Choropleth Quản trị",
    data=data,
    columns=["District", "Value"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Mức độ tiêu thụ (Tỷ đồng)"
).add_to(m)


m.save('map.html')
import webbrowser
webbrowser.open('map.html')