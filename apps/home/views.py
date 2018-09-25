from flask import Blueprint


home_blue = Blueprint('home', __name__)

@home_blue.route('/index/')
def index():
    return '首页'


@home_blue.route('/home/index1')
def index1():
    return '首页'
