import requests
from config import OPENWEATHER_API_KEY
from datetime import datetime

def get_weather(present_location):
    # Build the request URL using the OpenWeather API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={present_location}&appid={OPENWEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        # Extracting all relevant data from the JSON response
        weather_info = {
            'location': f"{data['name']}, {data['sys']['country']}",
            'temperature': {
                'current': f"{data['main']['temp']} °C",
                'feels_like': f"{data['main']['feels_like']} °C",
                'min': f"{data['main']['temp_min']} °C",
                'max': f"{data['main']['temp_max']} °C"
            },
            'weather_condition': data['weather'][0]['description'],
            'humidity': f"{data['main']['humidity']}%",
            'visibility': f"{data['visibility']} meters",
            'wind': {
                'speed': f"{data['wind']['speed']} m/s",
                'direction': f"{data['wind']['deg']} degrees"
            },
            'rain': f"{data.get('rain', {}).get('1h', 0)} mm/h" if 'rain' in data else 'No rain',
            'clouds': f"{data['clouds']['all']}%",
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return weather_info
    except requests.RequestException as e:
        return {'error': f"Request error: {str(e)}"}
    except ValueError as e:
        return {'error': f"JSON decode error: {str(e)}"}
