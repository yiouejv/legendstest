# coding=utf-8
from apps.common.views import common_bp
from flask import render_template


@common_bp.errorhandler(404)
def not_found_page(error):
    return render_template('common/404_page.html'), 404