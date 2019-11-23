import requests


#Был убран
weather_api = ''

def get_weather(city = 'Minsk'):
    data = dict()
    weather_city = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(weather_api, city)).json()
    data['city'] = weather_city['name']
    data['temp'] = weather_city['main']['temp']
    data['temp_max'] = weather_city['main']['temp_max']
    data['temp_min'] = weather_city['main']['temp_min']
    data['humidity'] = weather_city['main']['humidity']
    data['pressure'] = weather_city['main']['pressure']
    return data
