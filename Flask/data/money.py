import requests																		# Импорт библиотеки
from .config import url_money, url_money_for_base									# Импорт нужных данных из других файлов Python

course = requests.get(url_money).json()												# Парсинг курса валют


def get_money_for_base(date):														# Парсинг курса валют для базы данных
	date = date.split('-')
	url = url_money_for_base.format(day=date[0], month=date[1], year=date[2])
	r = requests.get(url).json()
	return r