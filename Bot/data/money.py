import requests


def get_money():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    return response
