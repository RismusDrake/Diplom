import requests
from bot import Bot

class MoviesBot(Bot):
	try:
		def __init__(self, token):
			super().__init__(token)
			self.money_url = 'https://afisha.tut.by/film'

		def get_movies(self):
			respone = requests.get(self.movies_url).json()










		except NameError:
		print('Name ошибка')
	except TypeError:
		print('Type ошибка')
	except ValueError:
		print('Value ошибка')
	except SyntaxError:
		print ('Syntax ошибка')
	except:
		print('Поймано исключение в классе "MoviesBot"')	
	finally:
		print('Конец поимки в классе "MoviesBot"')