import datetime
from flask import Flask, render_template, url_for
from data import get_weather
from data import course
from data import l_m


app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/weather')
def weather():
    return render_template('weather.html', time_now = datetime.datetime.now().date(), weather = get_weather())
print(get_weather())


@app.route('/courses')
def money():
    return render_template('money.html', time_now = datetime.datetime.now().date(), course = course)


@app.route('/movies')
def movies():
	return render_template('movies.html', time_now = datetime.datetime.now().date(), l_m = l_m)


if __name__ == '__main__':
	app.run(debug=True)