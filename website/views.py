from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html',user=current_user)


@views.route('/index.html')
def home2():
    return render_template('index.html')


@views.route('/profile')
@login_required
def profile():
    pass