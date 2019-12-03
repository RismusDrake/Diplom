import requests																			# Импортированные библиотеки
from bs4 import BeautifulSoup
from .config import url_movie															# Импорт нужных данных из других файлов Python


r = requests.get(url_movie)																# Ссылка на парсинг фильмов

soup = BeautifulSoup(r.text, 'lxml')													# Парсинг списка фильма
list_movies = soup.find('div', {'class': ['col-2 col-2-nobd']}).find('div', {'\
class': ['col-c']}).find('div', {'class': ['events-block js-cut_wrapper']}, id='\
events-block').find_all('li', {'class': ['lists__li']})
l_m = list()																			

for movie in list_movies:																# Создание цикла for
    m = dict()																			# Создание словаря
    m['name'] = movie.find('img').get('alt')											# Берем назывние фильма
    m['link'] = movie.find('a').get('href')												# Берем описание фильма
    m['image'] = movie.find('img').get('src')											# Берем картинку фильма
    m['info'] = movie.find('div').find('p').text 										# Берем инфу фильма
    l_m.append(m)																		# Добавляем все в список
l_m.pop(5)																				# Удаляем лишнее
l_m.pop(5)
l_m.pop(5)
l_m.pop(5)
l_m.pop(5)