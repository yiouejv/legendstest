# coding=utf-8
from config import session as db_session
from functools import wraps
from .views import front_bp
from flask import render_template, g, session
from apps.front.models import Student, Teacher
import config


@front_bp.before_request
def bind_user():
    '''在进入前端首页之前绑定用户'''
    if config.STUDENT_EMAIL in session:
        email = session[config.STUDENT_EMAIL]
        student_user = db_session.query(Student).filter(Student.student_email == email).first()
        if student_user:
            g.student_user = student_user

    if config.TEACHER_EMAIL in session:
        email = session[config.TEACHER_EMAIL]
        teacher_user = db_session.query(Teacher).filter(Teacher.teacher_email==email).first()
        if teacher_user:
            g.teacher_user = teacher_user



