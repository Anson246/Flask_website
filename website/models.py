from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Blog(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    title = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))


    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    blogper = db.relationship('Blog')

    
class Blogs(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # blog_id = db.Column(db.Integer, db.ForeignKey('user.blog.id'))
    blogall = db.relationship('Blog')
