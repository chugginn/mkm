from os import listdir
from os.path import isfile, join
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', videos=videos)


@app.route('/videos')
def videos():
    with open('yt/yt.txt') as f:
        videos1 = f.readlines()
        videos1 = [x.strip() for x in videos1]
    return render_template('videos.html', videos1=videos1)


@app.route('/shows')
def shows():
    return render_template('shows.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/photos')
def photos():
    photo_list = [f for f in listdir('static/img/gallery') if isfile(join('static/img/gallery', f))]
    return render_template('photos.html', photo_list=sorted(photo_list, reverse=True))


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
