from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv

from routes import commandes
from routes import users

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
app.register_blueprint(commandes.commandes_blueprint, url_prefix="/commandes")


if __name__ == '__main__':
    app.run(debug=True)
