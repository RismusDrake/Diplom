from flask import Flask, render_template
from data import movie


app = Flask(__name__)

global movie

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/movies/')
def movies():
	global movie
	movie = movie()
	return render_template('movies.html', movie=movie)


if __name__ == '__main__':
	app.run(debug=True)