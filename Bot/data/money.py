import requests																					# Импорт библиотеки
from .config import url_money																	# Импортирование данных из других файлов Python


def get_money():																				# Создание функции
    url = url_money																				# Ссылка на получение курса валют
    list_course = requests.get(url).json()
    l_c = list()																				# Создание пустого списка

    for course in list_course:																	# Создание цикла for
    	c = 'За ' + str(course.get('Cur_Scale')) + ' ' + course.get('Cur_Name') + '\
 (' + course.get('Cur_Abbreviation') + ') - ' + str(course.get('Cur_OfficialRate')) + ' BYN'	# Забираем интересующие нас данные
    	l_c.append(c)																			# Записываем данные в список
    return '\n'.join(l_c)																		# Завершение функции