import pymongo
import jsonpath
from flask import Flask, render_template, request, redirect, url_for
from pymongo.server_api import ServerApi

from blueprints import enter  # 添加蓝图
from blueprints import query
from blueprints import modify
from blueprints import delete
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import config
from flask_pymongo import PyMongo
from blueprints.link_app import link_login, link_register, link_edit

app = Flask(__name__)  # 这个默认值为templates
#-- 本地连接
app.config.from_object(config)
db = PyMongo(app).db
print(db)
# ---
app.register_blueprint(enter)  # 将所创建的蓝图添加到本文件中
app.register_blueprint(query)
app.register_blueprint(modify)
app.register_blueprint(delete)

#---
# mongo db 连接 云
# import pymongo
# from pymongo.server_api import ServerApi
#
# client = pymongo.MongoClient("mongodb+srv://localhost:27017123456@cluster0.dx6kiep.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client['Project6']
# user = db['user'].find()
# for i in user:
#    print(i)
#
# games = db['game'].find()
# for i in games:
#    print(i)
#-------
# @app.route('/login', methods = ['GET', 'POST'])
# def hello_world():  # put application's code here
#    return render_template('/login.html')
# GET：读取一个资源 get到一个html文件
# POST：页面点击 想让服务器做出请求
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    # print(user)
    # print(pwd)
    result = link_login(user, pwd)
    if result is True:
        return redirect('/menu')
    error = str(result)
    return render_template('login.html', error = error)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method =='POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        # print(user)
        # print(pwd)
        result = link_register(user, pwd)
        if result is True:     # 判断用户名是否以存在数据库中 有时间可添加一个函数 🌹
            return 'Successful <a href = "/">login</a>'
        else:
            error = str(result)
            return render_template('register.html', error=error)
    return render_template('register.html')

@app.route('/edit', methods =['GET', 'POST'])
def edit():
    if request.method == 'POST':
        user = request.form.get('user')
        opwd = request.form.get('old_pwd')
        npwd = request.form.get('new_pwd')
        # print(user)
        # print(opwd)
        # print(npwd)
        result = link_edit(user, opwd, npwd)
        if result is True:     # 判断用户名是否存在数据库中 有时间可添加一个判断函数 🌹
            return 'Successful <a href = "/">login</a>'
        else:
            error = str(result)
            return render_template('edit.html', error = error)
    return render_template('edit.html')

@app.route('/menu', methods=['GET', 'POST'])
def entry():
    return render_template('menu.html')

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    return render_template('add_menu.html')

@app.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query_menu.html')

@app.route('/modify', methods=['GET', 'POST'])
def modify():
    return render_template('modify_menu.html')

@app.route('/delete', methods=['GET', 'POST'])
def entry_delete():
    return render_template('delete_menu.html')

# print('url_map', app.url_map)
if __name__ == '__main__':
    print('url_map', app.url_map)
    app.run()
