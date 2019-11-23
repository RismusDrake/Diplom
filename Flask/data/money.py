import requests


url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
course = requests.get(url).json()
