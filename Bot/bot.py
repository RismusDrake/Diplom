import telebot
import pyowm
from pyowm.exceptions import OWMError
from data import bot_api, weather_api, get_money, l_c, get_movie


bot = telebot.TeleBot(bot_api)
owm = pyowm.OWM(weather_api, language = 'ru')

@bot.message_handler(commands=['start'])
def bot_hello(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	bot_help = telebot.types.InlineKeyboardButton('Помощь',callback_data='/help')
	keyboard.add(bot_help)
	bot.send_message(message.chat.id, 'Здравствуй пользователь, \
для получения команд напишите /help', reply_markup=keyboard)


@bot.callback_query_handler(lambda h: h.data == '/help')
def bot_help(callback_query: telebot.types.CallbackQuery):
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
	bot_weather = telebot.types.InlineKeyboardButton('Погода',callback_data='/weather')
	bot_courses_all = telebot.types.InlineKeyboardButton('Курс валют',callback_data='/courses_all')
	bot_movies = telebot.types.InlineKeyboardButton('Фильмы',callback_data='/movies')
	bot_location = telebot.types.InlineKeyboardButton("Геолокация", callback_data='/location')
	keyboard.add(bot_weather, bot_courses_all, bot_movies, bot_location)
	bot.send_message(callback_query.from_user.id, 'Команды на которые я смогу дать ответ: \n\
/weather - Узнать погоду \n/courses - Узнать курс валют на сегодня \n/course_usd - \
Узнать курс Доллара на сегодня \n/course_eur - Узнать курс Евро на сегодня \n\
/course_rub - Узнать курс Российского рубля на сегодня \n/course_uah - Узнать \
курс Гривен на сегодня \n/movies - Узнать какие фильмы сейчас идут \n/location - \
Узнать своё текущее местоположение', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_help(message):
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
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


@bot.callback_query_handler(lambda w: w.data == '/weather')
def bot_weather(callback_query: telebot.types.CallbackQuery):
	weathers = bot.send_message(callback_query.from_user.id, 'В каком городе вас интересует погода?')

	bot.register_next_step_handler(weathers, weather)

@bot.message_handler(commands=['weather'])
def send_weather(message):
	weathers = bot.send_message(message.chat.id, 'В каком городе вас интересует погода?')

	bot.register_next_step_handler(weathers, weather)

def weather(message):
	try:
		observation = owm.weather_at_place(message.text)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')['temp']
		bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас \
' + w.get_detailed_status()  + ', температура в среднем ' + str(temp) + ' градусов по Цельсию')
	except pyowm.exceptions.OWMError:
		answer = 'Прошу прощения, но я вас не понимаю, введите пожалуйста \
команду /weather и название города правильно'
		bot.send_message(message.chat.id, answer)


@bot.callback_query_handler(lambda c: c.data == '/courses_all')
def bot_course_all(callback_query: telebot.types.CallbackQuery):
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
	bot_courses = telebot.types.InlineKeyboardButton('Курc иностранной валюты',callback_data='/courses')
	course_usd = telebot.types.InlineKeyboardButton('Курc Доллара',callback_data='/course_usd')
	course_eur = telebot.types.InlineKeyboardButton('Курс Евро',callback_data='/course_eur')
	course_rub = telebot.types.InlineKeyboardButton('Курс Российского рубля',callback_data='/course_rub')
	course_uah = telebot.types.InlineKeyboardButton('Курс Гривен',callback_data='/course_uah')
	keyboard.add(bot_courses, course_usd, course_eur, course_rub, course_uah)
	bot.send_message(callback_query.from_user.id, 'Какой курс валют вас интересует?', reply_markup=keyboard)

@bot.callback_query_handler(lambda c: c.data == '/courses')
def bot_money(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) по отношению к \
иностранной валюте на сегодня: \n {money}')

@bot.message_handler(commands=['courses'])
def send_money(message):
	money = get_money()
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) по отношению к \
иностранной валюте на сегодня: \n {money}')


@bot.callback_query_handler(lambda c: c.data == '/course_usd')
def course_usd(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Доллару США на сегодня: \n {l_c[4]}')

@bot.message_handler(commands=['course_usd'])
def usd(message):
	money = get_money()		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Доллару США на сегодня: \n {l_c[4]}')


@bot.callback_query_handler(lambda c: c.data == '/course_eur')
def course_eur(callback_query: telebot.types.CallbackQuery):
	money = get_money()		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Евро на сегодня: \n {l_c[5]}')

@bot.message_handler(commands=['course_eur'])
def eur(message):
	money = get_money()		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Евро на сегодня: \n {l_c[5]}')


@bot.callback_query_handler(lambda c: c.data == '/course_rub')
def course_rub(callback_query: telebot.types.CallbackQuery):
	money = get_money()		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Российскому рублю на сегодня: \n {l_c[16]}')

@bot.message_handler(commands=['course_rub'])
def rub(message):
	money = get_money()	
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Российскому рублю на сегодня: \n {l_c[16]}')


@bot.callback_query_handler(lambda c: c.data == '/course_uah')
def course_uah(callback_query: telebot.types.CallbackQuery):
	money = get_money()	
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к \
Гривнам на сегодня: \n {l_c[2]}')

@bot.message_handler(commands=['course_uah'])
def uah(message):
	money = get_money()		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к \
Гривнам на сегодня: \n {l_c[2]}')


@bot.callback_query_handler(lambda m: m.data == '/movies')
def movies(callback_query: telebot.types.CallbackQuery):
	movies = get_movie()
	bot.send_message(callback_query.from_user.id, f'Показ фильмов на сегодня: \n{movies}')

@bot.message_handler(commands=['movies'])
def send_movies(message):
	movies = get_movie()
	bot.send_message(message.chat.id, f'Показ фильмов на сегодня: \n{movies}')


@bot.callback_query_handler(lambda l: l.data == '/location')
def bot_location(callback_query: telebot.types.CallbackQuery):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    location = telebot.types.KeyboardButton('Отправить местоположение', request_location=True)
    keyboard.add(location)
    bot.send_message(callback_query.from_user.id, 'Нажмите пожалуйста на кнопку для передачи своего местоположения', reply_markup=keyboard)

@bot.message_handler(commands=["location"])
def location(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
	location = telebot.types.KeyboardButton('Отправить местоположение', request_location=True)
	keyboard.add(location)
	bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку для передачи своего местоположения', reply_markup=keyboard)


bot.polling(none_stop=True, interval=1)