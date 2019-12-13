import requests																				# Импорт библиотеки
from .config import weather_api, url_weather												# Импорт ныжных данных из других файлов Python


def get_weather(city = 'Minsk'):
	weather = url_weather																	# Ссылка на парсинг погоды
	w = dict()																				# Создание словаря
	weather_city = requests.get(weather.format(weather_api, city)).json()					# Парсинг погоды
	w['city'] = weather_city['name']														# Берем название города
	w['temp'] = weather_city['main']['temp']												# Берем температуру
	w['humidity'] = weather_city['main']['humidity']										# Берем влажность
	w['pressure'] = weather_city['main']['pressure']										# Берем давление
	return w
