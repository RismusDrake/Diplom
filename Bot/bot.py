import requests
from bot_config import token

class Bot:
	try:
		def __init__(self, token):
			self.token = token
			self.url = f'https://api.telegram.org/bot{self.token}/'

		def get_updates(self):
			method = 'getUpdates'
			req = requests.get(self.url + method)
			return req.json()

		def get_message(self):
			data = self.get_updates()
			last_message = data['result'][-1]['message']
			chat_id = last_message['chat']['id']
			text = last_message['text']
			message = {'chat_id': chat_id,
					   'text': text}
			return message
		
		def send_message(self, chat_id, text):
			method = 'sendMessage'
			params = {'chat_id': chat_id,
					  'text': text}
			respone = requests.post(self.url + method, params)
			return respone


	except NameError:
		print('Name ошибка')
	except TypeError:
		print('Type ошибка')
	except ValueError:
		print('Value ошибка')
	except SyntaxError:
		print ('Syntax ошибка')
	except:
		print('Поймано исключение в классе "Bot"')
	finally:
		print('Конец поимки в классе "Bot"')