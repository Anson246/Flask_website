from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/blogs')
def blogs():
    return render_template('blogs.html')

@auth.route('/sign-up')
def signUp():
    return render_template('signup.html')

