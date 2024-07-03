from flask_restful import Resource, reqparse
from models import User
from db import db

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'name': user.name, 'email': user.email}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class UserListResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()

        new_user = User(name=args['name'], email=args['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}, 201
