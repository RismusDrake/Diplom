import telebot 																								# Импортирование библиотек
import pyowm
from pyowm.exceptions import OWMError
from data import bot_api, weather_api, get_money, get_movie											# Импортирование данных из других файлов Python


bot = telebot.TeleBot(bot_api)																				# Указываем какого бота запускать (API bot)
owm = pyowm.OWM(weather_api, language = 'ru')																# Запуск погоды (API weather)

@bot.message_handler(commands=['start'])																	# Получаем сообщение от бота при его запуске 
def bot_hello(message):																						# или выполнении команды /start
	keyboard = telebot.types.InlineKeyboardMarkup()															# Создание поля для кнопки
	bot_help = telebot.types.InlineKeyboardButton('Помощь',callback_data='/help')							# Создание кнопки для вывода помощи
	keyboard.add(bot_help)
	bot.send_message(message.chat.id, 'Здравствуй пользователь, \
для получения команд напишите /help', reply_markup=keyboard)


@bot.callback_query_handler(lambda h: h.data == '/help')													# Получаем сообщение от бота при
def bot_help(callback_query: telebot.types.CallbackQuery):													# выполнении команды /help через кнопку
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)												# Создание поля для кнопок и указываем их количество на одной строке
	bot_weather = telebot.types.InlineKeyboardButton('Погода',callback_data='/weather')						# Создание кнопки для вывода погоды
	bot_courses_all = telebot.types.InlineKeyboardButton('Курс валют',callback_data='/courses_all')			# Создание кнопки для вывода курса валют
	bot_movies = telebot.types.InlineKeyboardButton('Фильмы',callback_data='/movies')						# Содзание кнопки для вывода списка фильмов
	bot_location = telebot.types.InlineKeyboardButton("Геолокация", callback_data='/location')				# Создание кнопки для получения своей геолокации
	keyboard.add(bot_weather, bot_courses_all, bot_movies, bot_location)
	bot.send_message(callback_query.from_user.id, 'Команды на которые я смогу дать ответ: \n\
/weather - Узнать погоду \n/courses - Узнать курс валют на сегодня \n/course_usd - \
Узнать курс Доллара на сегодня \n/course_eur - Узнать курс Евро на сегодня \n\
/course_rub - Узнать курс Российского рубля на сегодня \n/course_uah - Узнать \
курс Гривен на сегодня \n/movies - Узнать какие фильмы сейчас идут \n/location - \
Узнать своё текущее местоположение', reply_markup=keyboard)

@bot.message_handler(commands=['help'])																		# Получаем сообщение от бота при
def send_help(message):																						# выполнении команды /help
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)												# Остальное повторяет что написано выше (21-25 строка)
	bot_weather = telebot.types.InlineKeyboardButton('Погода',callback_data='/weather')
	bot_courses_all = telebot.types.InlineKeyboardButton('Курс валют',callback_data='/courses_all')
	bot_movies = telebot.types.InlineKeyboardButton('Фильмы',callback_data='/movies')
	bot_location = telebot.types.InlineKeyboardButton("Геолокация", callback_data='/location')
	keyboard.add(bot_weather, bot_courses_all, bot_movies, bot_location)
	bot.send_message(message.chat.id, 'Команды на которые я смогу дать ответ: \n\
/weather - Узнать погоду \n/courses - Узнать курс валют на сегодня \n/course_usd - \
Узнать курс Доллара на сегодня \n/course_eur - Узнать курс Евро на сегодня \n\
/course_rub - Узнать курс Российского рубля на сегодня \n/course_uah - Узнать \
курс Гривен на сегодня \n/movies - Узнать какие фильмы сейчас идут \n/location - \
Узнать своё текущее местоположение', reply_markup=keyboard)


@bot.callback_query_handler(lambda w: w.data == '/weather')													# Получаем сообщение от бота при
def bot_weather(callback_query: telebot.types.CallbackQuery):												# выполнении команды /weather через кнопку
	weathers = bot.send_message(callback_query.from_user.id, 'В каком городе вас интересует погода?')		# Получаем выпрос от бота в каком городе нужно узнать погоду

	bot.register_next_step_handler(weathers, weather)														# Реагирование бота на ответ пользователя после его вопроса о городе

@bot.message_handler(commands=['weather'])																	# Получавем сообщение от бота при
def send_weather(message):																					# выполнении команды /weather
	weathers = bot.send_message(message.chat.id, 'В каком городе вас интересует погода?')					# Получаем выпрос от бота в каком городе нужно узнать погоду

	bot.register_next_step_handler(weathers, weather)														# Реагирование бота на ответ пользователя после его вопроса о городе

def weather(message):																						# Ответ бота на сообщение о городе пользователю
	try:																									# Ловим исключение
		observation = owm.weather_at_place(message.text)													# Работа юиюлиотеки PyOWM
		w = observation.get_weather()
		temp = w.get_temperature('celsius')['temp']															# Получаем информацию о температуре в цельсиях
		bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас \
' + w.get_detailed_status()  + ', температура в среднем ' + str(temp) + ' градусов по Цельсию')
	except pyowm.exceptions.OWMError:																		# Если пользователь введет неверное название города
		answer = 'Прошу прощения, но я вас не понимаю, введите пожалуйста \
команду /weather и название города правильно'
		bot.send_message(message.chat.id, answer)															# бот выдаст нам это сообщение


@bot.callback_query_handler(lambda c: c.data == '/courses_all')												# Получаем сообщение от бота
def bot_course_all(callback_query: telebot.types.CallbackQuery):											# при выполнении команды /courses через кнопку
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)												# Создание поля для кнопок и указывем их количество на одной строке
	bot_courses = telebot.types.InlineKeyboardButton('Курc иностранной валюты',callback_data='/courses')	# Создание кнопки для получения информации о курсе иностранной валюты
	course_usd = telebot.types.InlineKeyboardButton('Курc Доллара',callback_data='/course_usd')				# Создание кнопки для получения информации о курсе Доллара США
	course_eur = telebot.types.InlineKeyboardButton('Курс Евро',callback_data='/course_eur')				# Создание кнопки для получения информации о курсе Евро
	course_rub = telebot.types.InlineKeyboardButton('Курс Российского рубля',callback_data='/course_rub')	# Создание кнопки для получения информации о курсе Российского рубля
	course_uah = telebot.types.InlineKeyboardButton('Курс Гривен',callback_data='/course_uah')				#  Создание кнопки для получения информации о курсе Гривен
	keyboard.add(bot_courses, course_usd, course_eur, course_rub, course_uah)
	bot.send_message(callback_query.from_user.id, 'Какой курс валют вас интересует?', reply_markup=keyboard)

@bot.callback_query_handler(lambda c: c.data == '/courses')													# Получем сообщение от бота
def bot_money(callback_query: telebot.types.CallbackQuery):													# при выполнении команды из 78 строки
	money = get_money()
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) по отношению к \
иностранной валюте на сегодня: \n {money}')

@bot.message_handler(commands=['courses'])																	# Получаем сообщение от бота
def send_money(message):																					# при выполнении команды /courses
	money = get_money()
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) по отношению к \
иностранной валюте на сегодня: \n {money}')


@bot.callback_query_handler(lambda c: c.data == '/course_usd')												# Получаем сообщение от бота
def course_usd(callback_query: telebot.types.CallbackQuery):												# при выполнении команды /course_usd через кнопку
	money = get_money()
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Доллару США на сегодня: \n {money[152:187]}')

@bot.message_handler(commands=['course_usd'])																# Получаем сообщение от бота
def usd(message):																							# при выполнении команды /course_usd
	money = get_money()		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Доллару США на сегодня: \n {money[152:187]}')


@bot.callback_query_handler(lambda c: c.data == '/course_eur')												# Получаем сообщение от бота
def course_eur(callback_query: telebot.types.CallbackQuery):												# при выполнении команды /course_eur через кнопку
	money = get_money()		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Евро на сегодня: \n {money[187:215]}')

@bot.message_handler(commands=['course_eur'])																# Получаем сообщение от бота
def eur(message):																							# при выполнении команды /course_eur
	money = get_money()		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Евро на сегодня: \n {money[187:215]}')


@bot.callback_query_handler(lambda c: c.data == '/course_rub')												# Получаем сообщение от бота
def course_rub(callback_query: telebot.types.CallbackQuery):												# при выполнении команды /course_rub через кнопку
	money = get_money()		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Российскому рублю на сегодня: \n {money[616:659]}')

@bot.message_handler(commands=['course_rub'])																# Получаем сообщение от бота
def rub(message):																							# при выполнении команды /course_rub
	money = get_money()	
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Российскому рублю на сегодня: \n {money[616:659]}')


@bot.callback_query_handler(lambda c: c.data == '/course_uah')												# Получаем сообщение от бота
def course_uah(callback_query: telebot.types.CallbackQuery):												# при выполнении команды /course_uah через кнопку
	money = get_money()	
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Гривнам на сегодня: \n {money[81:113]}')

@bot.message_handler(commands=['course_uah'])																# Получаем сообщение от бота
def uah(message):																							# при выполнении команды /course_uah
	money = get_money()		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Гривнам на сегодня: \n {money[81:113]}')


@bot.callback_query_handler(lambda m: m.data == '/movies')													# Получаем сообщение от бота
def movies(callback_query: telebot.types.CallbackQuery):													# при выполнении команды /movies через кнопку
	movies = get_movie()
	bot.send_message(callback_query.from_user.id, f'Показ фильмов на сегодня: \n{movies}')

@bot.message_handler(commands=['movies'])																	# Получаем сообщение от бота
def send_movies(message):																					# при выполнении команды /movies
	movies = get_movie()
	bot.send_message(message.chat.id, f'Показ фильмов на сегодня: \n{movies}')


@bot.callback_query_handler(lambda l: l.data == '/location')												# Получаем сообщение от бота
def bot_location(callback_query: telebot.types.CallbackQuery):												# при выполнении команды /location через кнопку
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)												# Создание кнопки для пользователя
    location = telebot.types.KeyboardButton('Отправить местоположение', request_location=True)
    keyboard.add(location)
    bot.send_message(callback_query.from_user.id, 'Нажмите пожалуйста на кнопку для передачи своего местоположения', reply_markup=keyboard)

@bot.message_handler(commands=["location"])																	# Получаем сообщение от бота
def location(message):																						# при выполнении команды /location
	keyboard = telebot.types.ReplyKeyboardMarkup(True, True)												# Создание кнопки для пользователя
	location = telebot.types.KeyboardButton('Отправить местоположение', request_location=True)
	keyboard.add(location)
	bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку для передачи своего местоположения', reply_markup=keyboard)


bot.polling(none_stop=True, interval=3)																		# Завершение кода и интервал времени ответа бота на сообщение