# coding=utf-8
import config
from .views import admin_bp
from flask import session, g, render_template
from config import session as db_session
from apps.admin.models import Admin


@admin_bp.before_request
def bing_user():
    try:
        # 判断是否登陆，登陆了session中包含ADMIN_EMAIL键
        if config.ADMIN_UUID in session:
            admin_email = session.get(config.ADMIN_UUID)
            admin_user = db_session.query(Admin).filter(Admin.admin_email==admin_email).first()
            # 如果从数据库中查询到了user用户（以防存在假的cookie, 概率几乎没有）
            if admin_user:
                g.admin_user = admin_user
    except Exception as err:
        db_session.rollback()


@admin_bp.errorhandler(500)
def server_error(error):
    return render_template('admin/admin_error_500.html'), 500
