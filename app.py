from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS


from routes import users
from routes import tournees
from routes import creches
from routes import articles

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os


app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
jwt = JWTManager(app)


# Register routes
app.register_blueprint(users.users_blueprint, url_prefix="/users")
app.register_blueprint(tournees.bp_tournees, url_prefix="/tournees")
app.register_blueprint(creches.bp_creches, url_prefix="/creches")
app.register_blueprint(articles.bp_articles, url_prefix="/articles")

CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
