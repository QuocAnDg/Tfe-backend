from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS


from routes import users
from routes import tournees
from routes import creches

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os


app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
jwt = JWTManager(app)


# Register routes
app.register_blueprint(users.users_blueprint, url_prefix="/users")
app.register_blueprint(tournees.bp_tournees, url_prefix="/tournees")
app.register_blueprint(creches.bp_creches, url_prefix="/creches")


if __name__ == '__main__':
    app.run(debug=True)
