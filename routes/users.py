from flask import Blueprint, request, jsonify
from models import users
from flask_jwt_extended import create_access_token, jwt_required

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login', methods=['POST'])
def login():
    username_request = request.json.get("username", None)
    password_request = request.json.get("password", None)

    if username_request is None or username_request == "" or password_request is None or password_request == "":
        return jsonify({"msg": "Incorrect request"}), 400

    user_found = users.readoneuserfromusername(username_request)

    if len(user_found) == 0 or password_request != user_found[0]["user"]["password"]:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username_request)
    return jsonify(access_token=access_token, user=user_found[0]["user"])


@users_blueprint.route('/register', methods=['POST'])
@jwt_required()
def register():
    username_request = request.json.get("username", None)
    password_request = request.json.get("password", None)

    if username_request is None or username_request == "" or password_request is None or password_request == "":
        return jsonify({"msg": "Incorrect request"}), 400

    user_found = users.readoneuserfromusername(username_request)

    if len(user_found) != 0:
        return jsonify({"msg": "Username already existing"}), 406

    return users.createOne(username_request, password_request)

