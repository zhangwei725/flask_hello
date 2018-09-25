from flask import Blueprint

account = Blueprint('account', __name__)


# 函数是一等对象
# 万事万物皆对象
@account.route('/login/')
def login():
    return '登录'
