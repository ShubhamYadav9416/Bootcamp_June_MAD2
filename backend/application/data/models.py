from .database import db
from flask_security import UserMixin, RoleMixin


UserRoles = db.Table('UserRoles',
                     db.Column('user_id', db.ForeignKey('users.user_id')),
                     db.Column('role_id', db.ForeignKey('role.id')))

class Roles(db.Model,RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    name = db.Column(db.String(30), unique = True)
    description  = db.Column(db.String(200))

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_mail = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean)
    
    fs_uniquifier = db.Column(db.String(250), unique = True, nullable = False)
    
    roles = db.relationship('Roles', secondary = UserRoles,
                            backref = db.backref('users', lazy = 'dynamic'))


class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    movie_name = db.Column(db.String(50), nullable = False)
    movie_tag = db.Column(db.String(50), nullable = False)
    movie_lang = db.Column(db.String(50), nullable = False)
    movie_duration = db.Column(db.String(50), nullable = False)