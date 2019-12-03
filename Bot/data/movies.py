import requests																			# Импортированные библиотеки
from bs4 import BeautifulSoup
from .config import url_movie															# Импортирование данных из других файлов Python


def get_movie():																		# Создание функции
	r = requests.get(url_movie)															# Ссылка на получение списка фильмов

	soup = BeautifulSoup(r.text, 'lxml')												# Парсинг списка фильмов
	list_movies = soup.find('div', {'class': ['col-2 col-2-nobd']}).find('div', {'\
class': ['col-c']}).find('div', {'class': ['events-block js-cut_wrapper']}, id='\
events-block').find_all('a', {'class': ['name']})
	l_m = list()																		# Создание пустого листа

	for movie in list_movies:															# Создание цикла for
		m = movie.find('span').text 													# Берем нужные нам данные
		l_m.append(m)																	# Добавляем их в список
	l_m.pop(5)																			# Удаляем лишнее
	l_m.pop(5)
	l_m.pop(5)
	l_m.pop(5)
	l_m.pop(5)
	return '\n'.join(l_m)																# Завершение функции