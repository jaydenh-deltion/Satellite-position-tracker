import requests # voor het maken van HTTP verzoeken
from datetime import datetime # voor het werken met datums en tijden
import time # voor het toevoegen van vertragingen
from geopy.distance import geodesic # voor het berekenen van afstanden tussen coördinaten

print("🛰️  ISS POSITION TRACKER - LIVE") 
print("=" * 40) 
print(" Press Ctrl+C to stop the tracker ")
print()

dedemsvaart = (52.6003, 6.4631)

while True:
    response = requests.get("http://api.open-notify.org/iss-now.json") # dit is de API endpoint voor de ISS positie
    data = response.json() # parse de JSON response

    latitude = data['iss_position']['latitude'] # haal de latitude op
    longitude = data['iss_position']['longitude'] # haal de longitude op
    timestamp = data['timestamp'] # haal de timestamp op
    
    current_time = datetime.fromtimestamp(timestamp) # converteer timestamp naar leesbare tijd

    iss_position = (float(latitude), float(longitude))

    distance = geodesic(iss_position, dedemsvaart).kilometers # bereken de afstand tot Dedemsvaart

    print(f"Latitude: {latitude}° | Longitude:{longitude}° | Distance to Dedemsvaart : {distance:.0f} km| Time: {current_time}") # print de positie en tijd


    time.sleep(5) # wacht 5 seconden voordat je de volgende update ophaalt