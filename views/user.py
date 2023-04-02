from flask import request
from flask_restx import Resource, Namespace

from container import user_service
from dao.model.user import UserSchema
from utils import auth_required

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@user_ns.route('/<int:uid>')
class MovieView(Resource):

    def get(self, uid):
        b = user_service.get_one(uid)
        sm_d = UserSchema().dump(b)
        return sm_d, 200

    @auth_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route('/password/')
class UserView(Resource):
    def put(self):
        data = request.json
        password = data.get('password', None)
        if None in [password]:
            return '', 400

        passwords = user_service.update_password(password)
        return passwords, 201
