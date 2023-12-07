from flask import Flask, jsonify, request
from flask_cors import CORS
from neo4j import GraphDatabase
from dotenv import load_dotenv

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os

load_dotenv()

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

## Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
jwt = JWTManager(app)

# Neo4j configuration
uri = os.getenv('DB_URI')
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(username, password))


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username_request = request.json.get("username", None)
    password_request = request.json.get("password", None)

    if username_request != "test" or password_request != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.get('/users')
def get_users():
    query = "MATCH (user:User) RETURN user"
    with driver.session() as session:
        nodes = session.run(query).data()
    return jsonify(nodes)


@app.get('/commandes')
def get_commandes():
    query = "MATCH (commande:Commande) RETURN commande"
    with driver.session() as session:
        nodes = session.run(query).data()
    return jsonify(nodes)


if __name__ == '__main__':
    app.run(debug=True)
