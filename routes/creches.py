from flask import Blueprint, jsonify, request
from models import creches
from flask_jwt_extended import jwt_required

bp_creches = Blueprint('creches', __name__)


@bp_creches.route('/<nom>', methods=['GET'])
@jwt_required()
def get_creche(nom):
    return jsonify(creches.read_une_creche(nom))


@bp_creches.route('/<nom>', methods=['POST'])
@jwt_required()
def modify_creche(nom):
    new_articles = request.json.get("articles", None)
    return jsonify(creches.modify_creche(nom, new_articles))


@bp_creches.route('/changerstatut/<nom>', methods=['POST'])
@jwt_required()
def changer_statut(nom):
    new_statut = request.json.get("statut", None)
    return jsonify(creches.change_statut(nom, new_statut))
