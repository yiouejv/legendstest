from flask import render_template, views, session, redirect, url_for
from functools import wraps
import config


# 学生登陆验证
def student_login_required(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        if config.STUDENT_EMAIL in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("front.student_login"))
    return wraper


# 老师登陆验证
def teacher_login_required(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        if config.TEACHER_EMAIL in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("front.teacher_login"))
    return wraper

