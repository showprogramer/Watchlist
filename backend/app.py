from flask import Flask
from markupsafe import escape
from flask import url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello,flask!'

@app.route('/user/<name>')
def user_name(name):
    return f'hello,{escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_name',name='fanzehao'))
    print(url_for('user_name',name='fanzehao',query='123'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',query='123'))
    return 'test_url_for'
