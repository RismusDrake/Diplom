import requests
from bs4 import BeautifulSoup


url = 'https://afisha.tut.by/film/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
list_movies = soup.find('div', {'class': ['col-2 col-2-nobd']}).find('div', {'\
class': ['col-c']}).find('div', {'class': ['events-block js-cut_wrapper']}, id='\
events-block').find_all('li', {'class': ['lists__li']})
l_m = list()

for movie in list_movies:
    m = dict()
    m['name'] = movie.find('img').get('alt')
    m['link'] = movie.find('a').get('href')
    m['image'] = movie.find('img').get('src')
    m['info'] = movie.find('div').find('p').text
    l_m.append(m)
l_m.pop(5)
l_m.pop(5)
l_m.pop(5)
l_m.pop(5)
l_m.pop(5)