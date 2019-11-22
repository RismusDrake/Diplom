import requests
from bs4 import BeautifulSoup


url = 'https://afisha.tut.by/film/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

movies = soup.find('div', class_='events-block js-cut_wrapper').find_all('li')
list_movies = list()

for movie in movies:
    m = dict()
    m['name'] = movie.find('img').get('alt')
    m['link'] = movie.find('a').get('href')
    m['image'] = movie.find('img').get('src')
    m['info'] = movie.find('div').find('p').text
    list_movies.append(m)
