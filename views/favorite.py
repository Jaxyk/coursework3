from flask import request
from flask_restx import Resource, Namespace

from dao.model.favorite import Favorite_movieSchema
from container import favorite_service, movie_service, user_service

favorite_ns = Namespace('favorite')


@favorite_ns.route('/')
class FavoriteView(Resource):

    def get(self):
        rs = favorite_service.get_all()
        res = Favorite_movieSchema(many=True).dump(rs)
        return res, 200


@favorite_ns.route('/movies/<int:rid>')
class FavoriteView(Resource):
    def post(self, rid):
        req_json = request.json
        data= {
            "id": req_json["user_id"],
             "movie": movie_service.get_one(rid)
        }
        user_service.add_to_favorites(data)
        return "Movie added", 200

    def delete(self, rid):
        req_json = request.json
        data = {
            "id": req_json["user_id"],
            "movie": movie_service.get_one(rid)
        }
        user_service.remove_from_favorites(data)
        return "Movie delete", 201