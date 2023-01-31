
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
    code = request.form.get('code')
    x = requests.get(
        'https://api.weixin.qq.com/sns/jscode2session?appid=wx8d60bfc02a9179c2&secret=8fccb11216c2ef6c72711111b2163a19&js_code=' + code + '&grant_type=authorization_code')
    return x.json


@app.route('/msgCheck', methods=['POST'])
def msgCheck():
    content = request.form.get('content')
    data = {
        "scene": 1,
        "version": 2,
        "content": content
    }
    x = requests.post(
        'https://api.weixin.qq.com/wxa/msg_sec_check', data=data)
    return x.json()
