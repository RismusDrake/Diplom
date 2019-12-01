import requests
from .config import url_money, url_money_for_base

course = requests.get(url_money).json()


def get_money_for_base(date):
	date = date.split('-')
	url = url_money_for_base.format(day=date[0], month=date[1], year=date[2])
	r = requests.get(url).json()
	return r