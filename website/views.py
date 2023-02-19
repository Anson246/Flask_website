from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Blog, Blogs
from . import db
views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    return render_template('home.html', user=current_user)

@views.route('/blogs')
@login_required
def blogs():
    blogs = Blog.query.all()
    return render_template('blogs.html', user=current_user, blogs = blogs)

@views.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method =='POST':
        note = request.form.get('note')
        title = request.form.get('title')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_blog = Blogs()
            db.session.add(new_blog)
            db.session.commit()
            new_note = Blog(data = note, user_id=current_user.id, blog_id = 1, title = title)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('views.blogs'))
        
    return render_template('create.html', user=current_user, blogs = blogs)