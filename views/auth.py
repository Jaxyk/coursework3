from flask import request
from flask_restx import Resource, Namespace, abort

from container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)
        if None in [email, password]:
            abort(400)

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 200

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 200


@auth_ns.route('/register/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "Ok", 201
