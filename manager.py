# coding=utf-8
from flask import Flask
from apps.front.views import front_bp
from apps.admin.views import admin_bp
from apps.common.views import common_bp
from flask import render_template

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(front_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(common_bp)
# 更新配置
app.config.from_pyfile('config.py')


@app.errorhandler(404)
def not_found_page(error):
    return render_template('common/404_page.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')


