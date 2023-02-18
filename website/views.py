from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/blogs')
def blogs():
    return render_template('blogs.html')

@views.route('/sign-up')
def signUp():
    return render_template('signup.html')