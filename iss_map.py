import requests
import folium
import time 
from datetime import datetime

print("🛰️  ISS POSITION MAPPER - LIVE")
print("=" * 40)
print(" Creating live map of ISS position... ")

response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

latitude = float(data['iss_position']['latitude']) # haal de latitude op
longitude = float(data['iss_position']['longitude']) # haal de longitude op

dedemsvaart = [52.6003, 6.4631]

center_lat = (latitude + dedemsvaart[0]) / 2 # bereken het middenpunt voor de kaart
center_lon = (longitude + dedemsvaart[1]) / 2 # bereken het middenpunt voor de kaart

iss_map = folium.Map(location=[center_lat, center_lon], zoom_start=3) # maak de kaart aan

folium.Marker( # markeer de ISS positie
    [latitude, longitude],
    popup=f"ISS Position<br>Lat: {latitude}<br> Lon: {longitude}",
    icon=folium.Icon(color='red', icon='rocket', prefix='fa')
).add_to(iss_map)

folium.Marker( # markeer Dedemsvaart
    [52.6003, 6.4631],
    popup="Dedemsvaart",
    icon=folium.Icon(color='blue', icon='home', prefix='fa')
).add_to(iss_map)

folium.PolyLine( # teken een lijn tussen ISS en Dedemsvaart
    locations=[[latitude, longitude], dedemsvaart],
    color='blue',
    weight=3,
    opacity=0.8,
).add_to(iss_map)

iss_map.save("iss_map.html")

print("Map created and saved as iss_map.html")
