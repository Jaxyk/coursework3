from marshmallow import Schema, fields

from dao.model.genre import GenreSchema
from dao.model.movie import MovieSchema
from setup_db import db


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String)
	password = db.Column(db.String)
	username = db.Column(db.String)
	surname = db.Column(db.String)
	favorite_genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
	favorite_genre = db.relationship("Genre")
	favorite_movie = db.relationship("Movie", secondary="faivorite_movie", backref="users")


class UserSchema(Schema):
	id = fields.Int()
	email = fields.Str()
	password = fields.Str()
	username = fields.Str()
	surname = fields.Str()
	favorite_genre = fields.Pluck(GenreSchema, "name")
	favorite_movie = fields.Pluck(MovieSchema, "title", many=True)
