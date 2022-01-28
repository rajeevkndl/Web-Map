import folium

map1=folium.Map(location=[20.7503226,73.72543],zoom_start=4, tiles="Stamen Terrain", max_bounds=True)


fg_p=folium.FeatureGroup("population ranges in order Green< Blue < Yellow< Orange< Red for different countries")
fg_p.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<100000000 else 'blue' 
if 100000000<=x['properties']['POP2005']<=300000000 else 'yellow' if 300000000<=x['properties']['POP2005']<=600000000 else 'orange' if
600000000<=x['properties']['POP2005']<=1000000000 else 'red'}))

map1.add_child(fg_p)
map1.add_child(folium.LayerControl())
map1.save("map1.html")
