import requests
from .config import weather_api


def get_weather(city = 'Minsk'):
    w = dict()
    weather_city = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(weather_api, city)).json()
    w['city'] = weather_city['name']
    w['temp'] = weather_city['main']['temp']
    w['humidity'] = weather_city['main']['humidity']
    w['pressure'] = weather_city['main']['pressure']
    return w
