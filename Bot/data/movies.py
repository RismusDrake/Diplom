from random import sample as random_sample
import requests									# Импортированные библиотеки +
from bs4 import BeautifulSoup

from .config import MOVIES_URL					# Импортирование данных из других файлов Python +

def get_movies():		#-результат дает список фильмов, значит get_movies (множественное число)																# Создание функции
	r = requests.get(MOVIES_URL)				# Ссылка на получение списка фильмов 

	soup = BeautifulSoup(r.text, 'lxml')	# Парсинг списка фильмов +
	movies_in_xml = soup.find(				#-list_movies это список фильмов, а у нас сырой xml
		'div',								#-называем переменную чтобы ответить на вопрос "что это?"
		{'class': ['col-2 col-2-nobd']})
	movies_in_xml = movies_in_xml.find(		#-используем переносы, чтобы показать структура парсинга
		'div',
		{'class': ['col-c']})

	movies_in_xml = movies_in_xml.find(
		'div', 
		{'class': ['events-block js-cut_wrapper']}, 
		id='events-block')
	movies_in_xml = movies_in_xml.find_all(
		'a', 
		{'class': ['name']})

	movie_list = []											# Создание пустого листа -очевидно

	for movie in movies_in_xml:								# Создание цикла for -это видно из кода
		movie_list.append( movie.find('span').text  )		#-не PEP8, но компромисс между читаемостью и многословностью
		#-здесь довольно простой код, желательно не плодить временных переменных с неговорящим имененем						

	for item_to_remove in random_sample( movie_list, 5 ):	#-удаляем лишние 5(почему 5? магическое число. вынести в константу?) фильмов
		movie_list.remove( item_to_remove )					#-если все равно какие удалять - не хардкодим, а используем случайную выборку нужного размера

	# movie_list = [item for item in movie_list if item not in random_sample(movie_list, 5)] можно еще и так
	return '\n'.join(movie_list)							# Завершение функции -это очевидно

#-комментарии чаще не отвечают на вопрос "зачем?" а дублируют код
