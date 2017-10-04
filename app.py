from os import listdir
from os.path import isfile, join

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shows')
def shows():
    return render_template('shows.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


app.run(debug=True)
