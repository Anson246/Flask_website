from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import desc
from flask_login import login_required, current_user
from .models import Blog
from . import db
views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    return render_template('home.html', user=current_user)

@views.route('/blogs')
@login_required
def blogs():
    blogs = Blog.query.order_by(desc(Blog.date)).all()
    return render_template('blogs.html', user=current_user, blogs = blogs)

@views.route('/blogs/<int:id>')
@login_required
def blogview(id):
    blog = Blog.query.get(id = id).one()
    return render_template('blogview.html', blog = blog)

@views.route('/my-profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@views.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method =='POST':
        note = request.form.get('note')
        title = request.form.get('title')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            
            new_note = Blog(data = note, user_id=current_user.id, title = title)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('views.blogs'))
        
    return render_template('create.html', user=current_user, blogs = blogs)