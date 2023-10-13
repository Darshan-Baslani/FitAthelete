from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        login_password = request.form.get('login_password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, login_password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    
    return render_template('login.html', user=current_user)


@auth.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        signup_password1 = request.form.get('signup_password1')
        signup_password2 = request.form.get('signup_password2')
        
        user = User.query.filter_by(email=email).first()
        
        if email in user.email:
            flash('Email already Exists', category='error')
        elif '.' not in email:
            flash('Enter valid Email', category='error')
        elif len(email) < 5:
            flash('Enter valid Email', category='error')
        elif len(signup_password1) < 7:
            flash('Password should be greater than 7 character', category='error')
        elif signup_password1 != signup_password2:
            flash('Password Does Not Match', category='error')
        elif len(signup_password1) > 149:
            flash('Password is too long', category='error')
        elif len(email) > 149:
            flash('Email is too long', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(
                signup_password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))