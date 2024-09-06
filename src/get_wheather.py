import requests
from datetime import datetime, timedelta, timezone
from config import OPENWEATHER_API_KEY

def get_weather_forecast(present_location, time_zone_offset):
    # 获取地理坐标
    geocode_url = f"https://api.openweathermap.org/data/2.5/weather?q={present_location}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    try:
        # 请求当前天气数据以获取地理坐标
        response = requests.get(geocode_url)
        response.raise_for_status()
        data = response.json()
        
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        
        # 获取5天3小时预报
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        
        response = requests.get(forecast_url)
        response.raise_for_status()
        forecast_data = response.json()
        
        # 设置时区
        tz = timezone(timedelta(hours=time_zone_offset))
        
        today = datetime.now(tz).date()
        tomorrow = today + timedelta(days=1)
        
        today_and_current_forecast = []
        tomorrow_forecast = []
        
        # 当前天气
        current_weather = {
            'time': datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': f"{data['main']['temp']} °C",
            'feels_like': f"{data['main']['feels_like']} °C",
            'temp_min': f"{data['main']['temp_min']} °C",
            'temp_max': f"{data['main']['temp_max']} °C",
            'weather_condition': data['weather'][0]['description'],
            'humidity': f"{data['main']['humidity']}%",
            'wind': {
                'speed': f"{data['wind']['speed']} m/s",
                'direction': f"{data['wind']['deg']} degrees"
            },
            'rain': f"{data.get('rain', {}).get('1h', 0)} mm/h" if 'rain' in data else 'No rain',
            'clouds': f"{data['clouds']['all']}%"
        }
        
        today_and_current_forecast.append(current_weather)
        
        for entry in forecast_data['list']:
            dt = datetime.fromtimestamp(entry['dt'], tz)
            if dt.date() == today:
                today_and_current_forecast.append({
                    'time': dt.strftime('%Y-%m-%d %H:%M:%S'),
                    'temperature': f"{entry['main']['temp']} °C",
                    'feels_like': f"{entry['main']['feels_like']} °C",
                    'temp_min': f"{entry['main']['temp_min']} °C",
                    'temp_max': f"{entry['main']['temp_max']} °C",
                    'weather_condition': entry['weather'][0]['description'],
                    'humidity': f"{entry['main']['humidity']}%",
                    'wind': {
                        'speed': f"{entry['wind']['speed']} m/s",
                        'direction': f"{entry['wind']['deg']} degrees"
                    },
                    'rain': f"{entry.get('rain', {}).get('3h', 0)} mm/3h" if 'rain' in entry else 'No rain',
                    'clouds': f"{entry['clouds']['all']}%"
                })
            elif dt.date() == tomorrow:
                tomorrow_forecast.append({
                    'time': dt.strftime('%Y-%m-%d %H:%M:%S'),
                    'temperature': f"{entry['main']['temp']} °C",
                    'feels_like': f"{entry['main']['feels_like']} °C",
                    'temp_min': f"{entry['main']['temp_min']} °C",
                    'temp_max': f"{entry['main']['temp_max']} °C",
                    'weather_condition': entry['weather'][0]['description'],
                    'humidity': f"{entry['main']['humidity']}%",
                    'wind': {
                        'speed': f"{entry['wind']['speed']} m/s",
                        'direction': f"{entry['wind']['deg']} degrees"
                    },
                    'rain': f"{entry.get('rain', {}).get('3h', 0)} mm/3h" if 'rain' in entry else 'No rain',
                    'clouds': f"{entry['clouds']['all']}%"
                })
        
        # 返回当前天气和今天、明天的天气数据
        return {
            'today': today_and_current_forecast,
            'tomorrow': tomorrow_forecast
        }
    except requests.RequestException as e:
        return {'error': f"Request error: {str(e)}"}
    except ValueError as e:
        return {'error': f"JSON decode error: {str(e)}"}


# # 示例使用
# present_location = "Beijing"  # 替换为所需的地点
# time_zone_offset = 8  # 替换为所需的时区偏移
# forecast_data = get_weather_forecast(present_location, time_zone_offset)

# # 传递数据给目标函数
# today_data = forecast_data['today']
# tomorrow_data = forecast_data['tomorrow']
