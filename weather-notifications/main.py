import requests
from plyer import notification

#Get coordinates from city name
city = "Greece"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_params).json()

if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    #Get weather data
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_res = requests.get(weather_url, params=weather_params).json()

    if "current_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        weather_info = f"{city}: {temp}°C, Wind {wind} km/h"

        print("Weather:", weather_info)

        #Cross-platform notification
        notification.notify(
            title="Weather Update",
            message=weather_info,
            timeout=5
        )
    else:
        print("Weather data not found")
else:
    print("City not found")