import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def get_movies(html):
	soup = BeautifulSoup(html, 'lxml')
	list_movies = soup.find('div', {'class': ['col-2 col-2-nobd']}).find('div', {'class\
': ['col-c']}).find_all('ul', {'class': ['b-lists list_afisha col-5']})
	return [l_m.find('a', {'class': ['name']}).text for l_m in list_movies]

def movie():
	url = 'https://afisha.tut.by/film/'
	return get_movies(get_html(url))
