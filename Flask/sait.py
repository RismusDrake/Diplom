from flask import Flask, render_template, url_for							# Импорт библиотеки
from data import get_weather, course, l_m									# Импорт нужных данных из других файлов Python


app = Flask(__name__)														# Запуск Flask


@app.route('/')																# Что будем видеть при этом адресе
def home():
	return render_template('home.html')


@app.route('/weather')														# Что будем видеть при этом адресе
def weather():
    return render_template('weather.html', weather = get_weather())
print(get_weather())


@app.route('/courses')														# Что будем видеть при этом адресе
def money():
    return render_template('money.html', course = course)


@app.route('/movies')														# Что будем видеть при этом адресе
def movies():
	return render_template('movies.html', l_m = l_m)


if __name__ == '__main__':
	app.run(debug=True)