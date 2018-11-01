from flask import session, redirect, url_for
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.ADMIN_UUID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.admin_login'))
    return inner
