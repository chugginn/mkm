from os import listdir
from os.path import isfile, join

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open('/yt/yt.txt') as f:
        videos = f.readlines()
        videos = [x.strip() for x in videos]
    return render_template('index.html', videos=videos)


@app.route('/shows')
def shows():
    return render_template('shows.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/photos')
def photos():
    photo_list = [f for f in listdir('/static/img/gallery') if isfile(join('/static/img/gallery', f))]
    return render_template('photos.html', photo_list=sorted(photo_list, reverse=True))


@app.route('/contact')
def contact():
    return render_template('contact.html')


app.run(debug=True)
