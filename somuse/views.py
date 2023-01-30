
from somuse import app
from flask import render_template, request
import requests

@app.route('/')
def index():
    return render_template('index.html', user='user', super_user=False)


@app.route('/fullchain', methods=['GET', 'POST'])
def fullchain():
    lyrics = request.form.get('text')
    x = requests.post('https://somuse.asuscomm.com:88/fullchain', {'text': lyrics, 'ai': 'true', 'gender':'female'})
    return 'https://somuse.asuscomm.com:88/' + x.text

@app.route('/lyric', methods=['GET'])
def lyric():
    x = requests.get('https://somuse.asuscomm.com:88/lyric')
    return x.text