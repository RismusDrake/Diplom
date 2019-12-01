import requests
from .config import url_money


l_c = list()
def get_money():
    url = url_money
    list_course = requests.get(url).json()

    for course in list_course:
    	c = 'За ' + str(course.get('Cur_Scale')) + ' ' + course.get('Cur_Name') + '\
 (' + course.get('Cur_Abbreviation') + ') - ' + str(course.get('Cur_OfficialRate')) + ' BYN'
    	l_c.append(c)
    return '\n'.join(l_c)