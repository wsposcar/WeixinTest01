
from somuse import app
from flask import render_template, request
import requests


@app.route('/')
def index():
    return render_template('index.html', user='user', super_user=False)


@app.route('/fullchain', methods=['GET', 'POST'])
def fullchain():
    lyrics = request.form.get('text')
    x = requests.post('http://somuse.asuscomm.com:88/fullchain',
                      {'text': lyrics, 'ai': 'true', 'gender': 'female'})
    return 'https://somuse.asuscomm.com:88/' + x.text


@app.route('/lyric', methods=['GET'])
def lyric():
    x = requests.get('http://somuse.asuscomm.com:88/lyric')
    return x.text


@app.route('/auth', methods=['GET'])
def auth():
    x = request.get(
        'GET https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code')
    return x.json
