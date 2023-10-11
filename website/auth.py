from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    render_template('login.html')


@auth.route('/signup')
def signup():
    render_template('signup.html')