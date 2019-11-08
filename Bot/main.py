from money import MoneyBot
from bot_config import token
from bot import Bot
from weather import WeatherBot
# from movies import MoviesBot

try:
	courses_bot = MoneyBot(token)
	money = courses_bot.get_money()

	#Хочется чтобы, например, командой /course_usd бот выдавал курс валют только по доллару
	# money_usd = courses_bot.get_money()

	answer = courses_bot.get_message()
	weather_bot = WeatherBot(token)
	weather = weather_bot.get_weathers()
	answer = weather_bot.get_message()

	#Планы по созданию отдельного файла, связанного с парсингом фильмов
	# movies_bot = MoviesBot(token)
	# movies = movies_bot.get_movies()
	# answer = movies_bot.get_message()

	chat_id = answer['chat_id']
	text = answer['text']


	#Вывод курса валют
	if text == '/courses':
		courses_bot.send_message(chat_id, money)

	#Вывод отдельного курса валют
	# elif text == '/course_usd':
	#  	courses_bot.send_message(chat_id, money_usd)

	#Вывод погоды
	elif text == '/weather':
	# return f'В каком городе вас интересует погода?'
		weather_bot.send_message(chat_id, weather)


except NameError:
	print('Проблема с переменной')
except TypeError:
	print('Type ошибка')
except SyntaxError:
	print ('Syntax ошибка')
except KeyError:
	print ('KeyError ошибка')
except:
	print ('Поймано исключение в "main"')
finally:
	print('Конец поимки в файле "main"')