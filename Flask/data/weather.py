import requests																																	# Импорт библиотеки
from .config import weather_api																													# Импорт ныжных данных из других файлов Python


def get_weather(city = 'Minsk'):
    w = dict()																																	# Создание словаря
    weather_city = requests.get('http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(weather_api, city)).json()	# Парсинг погоды
    w['city'] = weather_city['name']																											# Берем название города
    w['temp'] = weather_city['main']['temp']																									# Берем температуру
    w['humidity'] = weather_city['main']['humidity']																							# Берем влажность
    w['pressure'] = weather_city['main']['pressure']																							# Берем давление
    return w
