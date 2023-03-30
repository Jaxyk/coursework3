from marshmallow import Schema, fields

from dao.model.movie import MovieSchema
from setup_db import db


class Favorite(db.Model):
    __tablename__ = 'faivorite_movie'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    favorite_movie = db.relationship("Movie")

class Favorite_movieSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    favorite_movie = fields.Pluck(MovieSchema, "title")
