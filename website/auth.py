from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/blogs')
def blogs():
    return render_template('blogs.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email=request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category="error")
        elif len(username) < 2:
            flash('Username must be greater than 2 characters', category="error")
        elif password1 != password2:
            flash('password do not match', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 7 characters', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html')

