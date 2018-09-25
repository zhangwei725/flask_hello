# Flask核心对象
from flask import Flask

# Flask框架核心类
# 每一个模块都是对应一个蓝图对象
from apps.account.views import account
from apps.home.views import home_blue


# 2
def create_app():
    # 3
    app = Flask(__name__)
    # 初始化蓝图对象
    # 4
    init_blue(app)
    init_ext(app)
    return app


# 注册蓝图对象
def init_blue(app):
    # 5
    app.register_blueprint(account)
    # 6
    app.register_blueprint(home_blue)


def init_ext(app):
    pass
