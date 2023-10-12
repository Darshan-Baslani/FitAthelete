from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')


@views.route('/index.html')
def home2():
    return render_template('index.html')