import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def get_movies(html):
	soup = BeautifulSoup(html, 'lxml')
	list_movies = soup.find('div', {'class': ['col-2 col-2-nobd']}).find('div', {'\
class': ['col-c']}).find('div', {'class': ['events-block js-cut_wrapper']}, id='\
events-block').find_all('a', {'class': ['name']})
	l_m = list()

	for movie in list_movies:
		m = movie.find('span').text
		l_m.append(m)
	l_m.pop(5)
	l_m.pop(5)
	l_m.pop(5)
	l_m.pop(5)
	l_m.pop(5)
	return ('\n'.join(l_m))

def movie():
	url = 'https://afisha.tut.by/film/'
	return get_movies(get_html(url))