import requests
import folium
import time 
from datetime import datetime

print("🛰️  ISS POSITION MAPPER - LIVE")
print("=" * 40)
print(" Creating live map of ISS position... ")

response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])

iss_map = folium.Map(location=[latitude, longitude], zoom_start=2)

folium.Marker(
    [latitude, longitude],
    popup=f"ISS Position<br>Lat: {latitude}<br> Lon: {longitude}",
    icon=folium.Icon(color='red', icon='rocket', prefix='fa')
).add_to(iss_map)

folium.Marker(
    [52.6003, 6.4631],
    popup="Dedemsvaart",
    icon=folium.Icon(color='blue', icon='home', prefix='fa')
).add_to(iss_map)

iss_map.save("iss_live_map.html")

print("Map created and saved as iss_map.html")
