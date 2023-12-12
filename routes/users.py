from flask import Blueprint, request, jsonify
from models import users
from flask_jwt_extended import create_access_token, jwt_required

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login', methods=['POST'])
def login():
    username_request = request.json.get("username", None)
    password_request = request.json.get("password", None)

    user_found = users.readoneuserfromusername(username_request)

    if len(user_found) == 0 or len(username_request) == 0 or password_request != user_found[0]["user"]["password"]:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username_request)
    return jsonify(access_token=access_token)


@users_blueprint.route('/register', methods=['POST'])
@jwt_required()
def register():
    username_request = request.json.get("username", None)
    password_request = request.json.get("password", None)

    user_found = users.readoneuserfromusername(username_request)

    if len(user_found) != 0 or len(username_request) == 0:
        return jsonify({"msg": "Username already existing"}), 401

    return users.createOne(username_request, password_request)

