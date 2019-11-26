import telebot
import pyowm
from data import bot_api, weather_api
from data import get_money
from data import get_movie


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
	weathers = bot.send_message(callback_query.from_user.id, 'В каком районе вас интересует погода?')

	bot.register_next_step_handler(weathers, weather)

@bot.message_handler(commands=['weather'])
def send_weather(message):
	weathers = bot.send_message(message.chat.id, 'В каком районе вас интересует погода?')

	bot.register_next_step_handler(weathers, weather)

def weather(message):
	try:
		observation = owm.weather_at_place(message.text)
		if observation == False:
			bot.send_message(message.chat.id, 'Ничего')				#Отвечает за работу исключения
		else:
			w = observation.get_weather()
			temp = w.get_temperature('celsius')['temp']
			bot.send_message(message.chat.id, 'В районе ' + message.text + ' сейчас \
' + w.get_detailed_status()  + ', температура в среднем ' + str(temp) + ' градусов по Цельсию')
	except Exception:
		answer = 'Прошу прощения, но я вас не понимаю, введите пожалуйста \
команду /weather и название района правильно'
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
def bot_courses(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'AUD':
			aud_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'BGN':
			bgn_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'UAH':
			uah_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'DKK':
			dkk_price = p['Cur_OfficialRate']		
		elif p['Cur_Abbreviation'] == 'USD':
			usd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'EUR':
			eur_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'PLN':
			pln_price = p['Cur_OfficialRate']	
		elif p['Cur_Abbreviation'] == 'IRR':
			irr_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'ISK':
			isk_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'JPY':
			jpy_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CAD':
			cad_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CNY':
			cny_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'KWD':
			kwd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'MDL':
			mdl_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'NZD':
			nzd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'NOK':
			nok_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'RUB':
			rub_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'XDR':
			xdr_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'SGD':
			sgd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'KGS':
			kgs_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'KZT':
			kzt_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'TRY':
			try_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'GBP':
			gbp_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CZK':
			czk_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'SEK':
			sek_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CHF':
			chf_price = p['Cur_OfficialRate']
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) по отношению к иностранной валюте на сегодня: \n\
1 Австралийский доллар (AUD) за {aud_price} BYN \n1 Болгарский лев (BGN) за {bgn_price} BYN \n100 Гривен (UAH) за {uah_price} BYN \n\
10 Датских крон (DKK) за {dkk_price} BYN \n1 Доллар США (USD) за {usd_price} BYN \n1 Евро (EUR) за {eur_price} BYN \n10 Злотых (PLN) за \
{pln_price} BYN \n100000 Иранских риал (IRR) за {irr_price} BYN \n100 Исландских крон (ISK) за {isk_price} BYN \n100 Йен (JPY) за {jpy_price} \
BYN \n1 Канадский доллар (CAD) за {cad_price} BYN \n10 Китайских юаней (CNY) за {cny_price} BYN \n1 Кувейтский динар (KWD) за {kwd_price} BYN \n\
10 Молдавских лей (MDL) за {mdl_price} BYN \n1 Новозеландский доллар (NZD) за {nzd_price} BYN \n10 Норвежских крон (NOK) за {nok_price} BYN \n\
100 Российских рублей (RUB) за {rub_price} BYN \n1 СДР (Специальные права заимствования) (XDR) за {xdr_price} BYN \n1 Сингапурский доллар \
(SGD) за {sgd_price} BYN \n100 Сом (KGS) за {kgs_price} BYN \n1000 Тенге (KZT) за {kzt_price} BYN \n10 Турецких лир (TRY) за {try_price} BYN \n\
1 Фунт стерлингов (GBP) за {gbp_price} BYN \n100 Чешских крон (CZK) за {czk_price} BYN \n10 Шведских крон (SEK) за {sek_price} BYN \n\
1 Швейцарский франк (CHF) за {chf_price} BYN')

@bot.message_handler(commands=['courses'])
def send_money(message):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'AUD':
			aud_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'BGN':
			bgn_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'UAH':
			uah_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'DKK':
			dkk_price = p['Cur_OfficialRate']		
		elif p['Cur_Abbreviation'] == 'USD':
			usd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'EUR':
			eur_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'PLN':
			pln_price = p['Cur_OfficialRate']	
		elif p['Cur_Abbreviation'] == 'IRR':
			irr_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'ISK':
			isk_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'JPY':
			jpy_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CAD':
			cad_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CNY':
			cny_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'KWD':
			kwd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'MDL':
			mdl_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'NZD':
			nzd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'NOK':
			nok_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'RUB':
			rub_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'XDR':
			xdr_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'SGD':
			sgd_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'KGS':
			kgs_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'KZT':
			kzt_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'TRY':
			try_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'GBP':
			gbp_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CZK':
			czk_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'SEK':
			sek_price = p['Cur_OfficialRate']
		elif p['Cur_Abbreviation'] == 'CHF':
			chf_price = p['Cur_OfficialRate']
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) по отношению к иностранной валюте на сегодня: \n\
1 Австралийский доллар (AUD) за {aud_price} BYN \n1 Болгарский лев (BGN) за {bgn_price} BYN \n100 Гривен (UAH) за {uah_price} BYN \n\
10 Датских крон (DKK) за {dkk_price} BYN \n1 Доллар США (USD) за {usd_price} BYN \n1 Евро (EUR) за {eur_price} BYN \n10 Злотых (PLN) за \
{pln_price} BYN \n100000 Иранских риал (IRR) за {irr_price} BYN \n100 Исландских крон (ISK) за {isk_price} BYN \n100 Йен (JPY) за {jpy_price} \
BYN \n1 Канадский доллар (CAD) за {cad_price} BYN \n10 Китайских юаней (CNY) за {cny_price} BYN \n1 Кувейтский динар (KWD) за {kwd_price} BYN \n\
10 Молдавских лей (MDL) за {mdl_price} BYN \n1 Новозеландский доллар (NZD) за {nzd_price} BYN \n10 Норвежских крон (NOK) за {nok_price} BYN \n\
100 Российских рублей (RUB) за {rub_price} BYN \n1 СДР (Специальные права заимствования) (XDR) за {xdr_price} BYN \n1 Сингапурский доллар \
(SGD) за {sgd_price} BYN \n100 Сом (KGS) за {kgs_price} BYN \n1000 Тенге (KZT) за {kzt_price} BYN \n10 Турецких лир (TRY) за {try_price} BYN \n\
1 Фунт стерлингов (GBP) за {gbp_price} BYN \n100 Чешских крон (CZK) за {czk_price} BYN \n10 Шведских крон (SEK) за {sek_price} BYN \n\
1 Швейцарский франк (CHF) за {chf_price} BYN')


@bot.callback_query_handler(lambda c: c.data == '/course_usd')
def course_usd(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'USD':
			usd_price = p['Cur_OfficialRate']		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к Доллару (USD) на сегодня: \n1 USD за {usd_price} BYN')

@bot.message_handler(commands=['course_usd'])
def usd(message):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'USD':
			usd_price = p['Cur_OfficialRate']		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к Доллару (USD) на сегодня: \n1 USD за {usd_price} BYN')


@bot.callback_query_handler(lambda c: c.data == '/course_eur')
def course_usd(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	for p in list(money):
			if p["Cur_Abbreviation"] == 'EUR':
				eur_price = p['Cur_OfficialRate']		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к Евро (EUR) на сегодня: \n1 EUR за {eur_price} BYN')

@bot.message_handler(commands=['course_eur'])
def eur(message):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'EUR':
			eur_price = p['Cur_OfficialRate']		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к Евро (EUR) на сегодня: \n1 EUR за {eur_price} BYN')


@bot.callback_query_handler(lambda c: c.data == '/course_rub')
def course_usd(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'RUB':
			rub_price = p['Cur_OfficialRate']		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к Российскому рублю (RUB) на сегодня: \n100 RUB за {rub_price} BYN')

@bot.message_handler(commands=['course_rub'])
def rub(message):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'RUB':
			rub_price = p['Cur_OfficialRate']		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к Российскому рублю (RUB) на сегодня: \n100 RUB за {rub_price} BYN')


@bot.callback_query_handler(lambda c: c.data == '/course_uah')
def course_usd(callback_query: telebot.types.CallbackQuery):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'UAH':
			uah_price = p['Cur_OfficialRate']		
	bot.send_message(callback_query.from_user.id, f'Курс Белорусского рубля (BYN) к Гривнам (UAH) на сегодня: \n100 UAH за {uah_price} BYN')

@bot.message_handler(commands=['course_uah'])
def uah(message):
	money = get_money()
	for p in list(money):
		if p["Cur_Abbreviation"] == 'UAH':
			uah_price = p['Cur_OfficialRate']		
	bot.send_message(message.chat.id, f'Курс Белорусского рубля (BYN) к Гривнам (UAH) на сегодня: \n100 UAH за {uah_price} BYN')


@bot.callback_query_handler(lambda m: m.data == '/movies')
def course_usd(callback_query: telebot.types.CallbackQuery):
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
    bot.send_message(callback_query.from_user.id, 'Нажмите пожалуйста на кнопку для передачи своей геолокации', reply_markup=keyboard)

@bot.message_handler(commands=["location"])
def location(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
	location = telebot.types.KeyboardButton('Отправить местоположение', request_location=True)
	keyboard.add(location)
	bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку для передачи своей геолокации', reply_markup=keyboard)


bot.polling(none_stop=True, interval=2)
