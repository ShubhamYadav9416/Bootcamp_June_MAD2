from .database import db

class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    movie_name = db.Column(db.String(50), nullable = False)
    movie_tag = db.Column(db.String(50), nullable = False)
    movie_lang = db.Column(db.String(50), nullable = False)
    movie_duration = db.Column(db.String(50), nullable = False)