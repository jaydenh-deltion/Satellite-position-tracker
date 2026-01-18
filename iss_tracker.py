import requests
from datetime import datetime
import time

print("🛰️  ISS POSITION TRACKER - LIVE")
print("=" * 40)
print(" Press Ctrl+C to stop the tracker ")
print()

while True:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    
    current_time = datetime.fromtimestamp(timestamp)

    print(f"Latitude: {latitude}° | Longitude:){longitude}° | Time: {current_time}")


    time.sleep(5)