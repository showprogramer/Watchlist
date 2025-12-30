from flask import Flask, render_template
from markupsafe import escape
from flask import url_for
import os

# 获取上级目录的 fronted 文件夹
template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fronted')
app = Flask(__name__, template_folder=template_dir)

print(os.path.dirname(os.path.dirname(__file__)))

#模拟数据
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/index')
def index():
    return render_template('index.html', name=name, movies=movies)

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
