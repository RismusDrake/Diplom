import pymysql																						# Импортированные библиотеки
import requests
import re
from bs4 import BeautifulSoup
from data import base_url_weather, get_money_for_base, base_url_movie								# Импортирование данных из других файлов Python


def get_connection():																				# Подключение к MySql
    return pymysql.connect(host='localhost',
        				   user='root',
        				   password=Romaric123Romaric,
       				   	   charset='utf8mb4',
        				   db='flask_base',
        				   cursorclass=pymysql.cursors.DictCursor)

 
def weather_base(cursor):																			# Создание таблицы для погоды, её запись и завершение записи
	url = base_url_weather
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	list_weather = soup.find('div', {'class': ['b-future']}).text
	cursor.execute('INSERT INTO weather (day, time, temp) VALUES (%s, %s, %s)', list_weather)

	con = get_connection()
	try:
		with con.cursur() as cursor:
			cursor.execute('select day, time, temp from weather')
			return cursor.fetchall()
	finally:
		con.close()


def money_base(day, month, year, cursor):															# Создание таблицы для курса валют, её запись и завершение записи
	list_courses = get_money_for_base(f'{day}-{month}-{year}')
	for course in list_course:
		c = ('За ' + str(course('Cur_Scale')) + ' ' + course('Cur_Name') + '\
(' + course.get('Cur_Abbreviation') + ') - ' + str(course.get('Cur_OfficialRate')) + ' BYN')
		cursor.execute('INSERT INTO money (name, course) VALUES (%s, %s)', c)

	con = get_connection()
	try:
		with con.cursor() as cursor:
			cursor.execute('select name, course from money')
			return cursor.fetchall()
	finally:
		con.close()


def movie_base(cursor):																				# Создание таблицы для списка фильмов, её запись и завершение записи
	url = base_url_movie
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	list_movies = soup.find('div', {'class': ['floate\
r-content']}).find('div', {'class': ['middle']}).find('div\
', {'class': ['el4ed ml10 ilb']}).find_all('div', {'class': ['c\
ontent br5 new_release']})[307:453]
	l_m = list()
	for movie in list_movies:
		n = movie.find('div', {'class': ['date']}).text
		m = movie.find('h2').text
		d = re.sub(r'\s', '', n)
		l_m.append(m + ' ' + d)
	cursor.execute('INSERT INTO movie (name, date) VALUES (%s, %s)', l_m)

	con = get_connection()
	try:
		with con.cursur() as cursor:
			cursor.execute('select name, date from movie')
			return cursor.fetchall()
	finally:
		con.close()