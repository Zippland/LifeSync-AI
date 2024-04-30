import requests
from config import PRESENT_LOCATION, DEFINE_DATE
from datetime import datetime

def get_weather(location = PRESENT_LOCATION, date = DEFINE_DATE):
    # Replace 'YOUR_WEATHER_API_KEY' with your actual weather API key
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")  # Default to today's date if not specified
    url = f"http://api.weatherapi.com/v1/forecast.json?key=YOUR_WEATHER_API_KEY&q={location}&dt={date}&days=1&aqi=yes&alerts=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        # Check if 'forecast' and 'forecastday' keys are in the response data
        if 'forecast' in data and 'forecastday' in data['forecast']:
            forecast = data['forecast']['forecastday'][0]
            return {
                'temperature_range': f"{forecast['day']['mintemp_c']} to {forecast['day']['maxtemp_c']} °C",
                'apparent_temperature': f"{forecast['day']['avgtemp_feelslike_c']} °C",
                'humidity': forecast['day']['avghumidity'],
                'air_quality': forecast['day']['condition']['text'],
                'uv_index': forecast['day']['uv'],
                'will_it_rain': forecast['day']['daily_will_it_rain'],
                'rain_periods': [(hour['time'], hour['will_it_rain']) for hour in forecast['hour'] if hour['will_it_rain']]
            }
        else:
            return {'error': 'Forecast data not found in the API response'}

    except requests.RequestException as e:
        return {'error': f"Request error: {str(e)}"}
    except ValueError as e:
        return {'error': f"JSON decode error: {str(e)}"}