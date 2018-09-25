from flask_script import Manager, Server

# 蓝图对象前后端不分离的项目中
from apps import create_app

# 直接引入映入app对象可能会出现循环引入的问题
"""
第一步下载插件
第二歩实例化插件对象
第二歩 注册
# init_app()
第四歩使用
"""
app = create_app()

manager = Manager(app=app)

#  添加脚本命令
manager.add_command('run', Server(host='127.0.0.1', port=9000, use_debugger=True))
"""=====蓝图对象======"""

# 拆分成一个个的功能
# 不方便维护
# 不方便团队开发 ---> 文件冲突

# 视图函数
# @app_blueprint.route('/')  # 路由
# def index():
#     # 加入数据库操作
#     return '欢迎来到首页'


# apps
# @app_blueprint.route('/account/login/')
# def login():
#     return '登录界面'


# @app_blueprint.route('/account/register/')
# def register():
#     return '注册界面'


# 修改
if __name__ == '__main__':
    manager.run()
