from flask import Flask
from flask_restful import Api
from config import Config
from db import db

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db.init_app(app)

from resources.user import UserResource, UserListResource
from resources.selenium import SeleniumResource

api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(UserListResource, '/user')
api.add_resource(SeleniumResource, '/selenium')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
