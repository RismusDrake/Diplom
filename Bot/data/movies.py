import requests
from bs4 import BeautifulSoup


def get_movie():
	url = 'https://afisha.tut.by/film/'
	r = requests.get(url)

	soup = BeautifulSoup(r.text, 'lxml')
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
	return '\n'.join(l_m)
