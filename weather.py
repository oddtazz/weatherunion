# Importing requests library for making HTTP requests and json library for working with JSON data
import requests
import json

# Function to get weather data for a specific location using an API key
def get_weather_data(location, api_key):
    url = f"https://www.weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id={location}"
    headers = {"x-zomato-api-key": api_key}

    # Sending GET request to the API endpoint with provided headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Read API key and location from config.json
with open('config.json') as f:
    config = json.load(f)
    location = config['location']
    api_key = config['api_key']

# Getting weather data using provided location and API key
weather_data = get_weather_data(location, api_key)
if weather_data:
    locality_weather_data = weather_data.get("locality_weather_data")
    if locality_weather_data:
        humidity = locality_weather_data.get("humidity")
        wind_speed = locality_weather_data.get("wind_speed")
        temperature = locality_weather_data.get("temperature")
        wind_direction = locality_weather_data.get("wind_direction")
        rain_intensity = locality_weather_data.get("rain_intensity")
        rain_accumulation = locality_weather_data.get("rain_accumulation")

        # Printing weather details
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
        print(f"Wind Direction: {wind_direction} Degrees")
        print(f"Rain Intensity: {rain_intensity} mm/min")
        print(f"Total Rainfall: {rain_accumulation} mm")