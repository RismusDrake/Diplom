import pyowm
from bot import Bot
from weather_config import api


#Тут запускать бесполезно, ничего не выводит, запускать через main
class WeatherBot(Bot):
	try:
		def get_weathers(self):
			owm = pyowm.OWM(api, language = 'ru')

			#Надо чтобы это спрашивал бот и отвечал нам соответствующе
			place = input('В каком городе вас интересует погода?: ')

			observation = owm.weather_at_place(place)
			w = observation.get_weather()

			temp = w.get_temperature('celsius')['temp']

			return f'В городе {place} сейчас {w.get_detailed_status()}, температура в среднем {temp} градусов по Цельсию'


	except NameError:
		print('Name ошибка')
	except TypeError:
		print('Type ошибка')
	except ValueError:
		print('Value ошибка')
	except SyntaxError:
		print ('Syntax ошибка')
	except:
		print('Поймано исключение в классе "WeatherBot"')	
	finally:
		print('Конец поимки в классе "WeatherBot"')
