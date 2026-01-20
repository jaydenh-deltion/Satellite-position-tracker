import requests
import folium 
import time
from datetime import datetime

print("🛰️  ISS TRAIL TRACKER")
print("=" * 40)
print(" Tracking ISS movement. this wil take a few moments... ")

dedemsvaart = [52.6003, 6.4631]
trail_positions = []

for i in range(6):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    