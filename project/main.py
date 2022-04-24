# main.py

from flask import Blueprint, render_template, request, session, abort, current_app
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/loader')
def loader():
    return render_template('loader.html'), {"Refresh": "3; url=http://127.0.0.1:5000/conteiner"}


@main.route('/conteiner')
def conteiner():
    return render_template('index.html')


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    name = current_user.name
    return render_template('profile.html', name=name)
