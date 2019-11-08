import requests
from bot import Bot

class MoneyBot(Bot):
	try:
		def __init__(self, token):
			super().__init__(token)
			self.money_url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

		def get_money(self):
			respone = requests.get(self.money_url).json()
			aud_price = bgn_price = uah_price = dkk_price = usd_price = eur_price = pln_price = irr_price = isk_price = jpy_price = cad_price = cny_price = kwd_price = mdl_price = nzd_price = nok_price = rub_price = xdr_price = sgd_price = kgs_price = kzt_price = try_price = gbp_price = czk_price = sek_price = chf_price = 'NOT_FOUND' 
			for p in list(respone):
				if p['Cur_Abbreviation'] == 'AUD':
					aud_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'BGN':
					bgn_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'UAH':
					uah_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'DKK':
					dkk_price = p['Cur_OfficialRate']		
				if p['Cur_Abbreviation'] == 'USD':
					usd_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'EUR':
					eur_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'PLN':
					pln_price = p['Cur_OfficialRate']	
				if p['Cur_Abbreviation'] == 'IRR':
					irr_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'ISK':
					isk_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'JPY':
					jpy_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'CAD':
					cad_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'CNY':
					cny_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'KWD':
					kwd_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'MDL':
					mdl_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'NZD':
					nzd_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'NOK':
					nok_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'RUB':
					rub_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'XDR':
					xdr_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'SGD':
					sgd_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'KGS':
					kgs_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'KZT':
					kzt_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'TRY':
					try_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'GBP':
					gbp_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'CZK':
					czk_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'SEK':
					sek_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'CHF':
					chf_price = p['Cur_OfficialRate']
			return f'Курс Белорусского рубля (BYN) по отношению к иностранной валюты на сегодня согласно НБРБ: 1 Австралийский доллар (AUD) - {aud_price} BYN, 1 Болгарский лев (BGN) - {bgn_price} BYN, \
100 Гривен (UAH) - {uah_price} BYN, 10 Датских крон (DKK) - {dkk_price} BYN, 1 Доллар США (USD) - {usd_price} BYN, 1 Евро (EUR) - {eur_price} BYN, 10 Злотых (PLN) - {pln_price} BYN, \
100000 Иранских риал (IRR) - {irr_price} BYN, 100 Исландских крон (ISK) - {isk_price} BYN, 100 Йен (JPY) - {jpy_price} BYN, 1 Канадский доллар (CAD) - {cad_price} BYN, 10 Китайских юаней (CNY) - {cny_price} BYN, \
1 Кувейтский динар (KWD) - {kwd_price} BYN, 10 Молдавских лей (MDL) - {mdl_price} BYN, 1 Новозеландский доллар (NZD) - {nzd_price} BYN, 10 Норвежских крон (NOK) - {nok_price} BYN, 100 Российских рублей (RUB) - {rub_price} BYN, \
1 СДР (Специальные права заимствования) (XDR) - {xdr_price} BYN, 1 Сингапурский доллар (SGD) - {sgd_price} BYN, 100 Сом (KGS) - {kgs_price} BYN, 1000 Тенге (KZT) - {kzt_price} BYN, 10 Турецких лир (TRY) - {try_price} BYN, \
1 Фунт стерлингов (GBP) - {gbp_price} BYN, 100 Чешских крон (CZK) - {czk_price} BYN, 10 Шведских крон (SEK) {sek_price} BYN, 1 Швейцарский франк (CHF) {chf_price} BYN'


	except NameError:
		print('Name ошибка')
	except TypeError:
		print('Type ошибка')
	except ValueError:
		print('Value ошибка')
	except SyntaxError:
		print ('Syntax ошибка')
	except:
		print('Поймано исключение в классе "MoneyBot"')	
	finally:
		print('Конец поимки в классе "MoneyBot"')