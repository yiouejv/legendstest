#encoding: utf-8

from flask import Blueprint, render_template

common_bp = Blueprint('common', __name__, url_prefix='/common')


@common_bp.route('/')
def login():
    return 'common index'