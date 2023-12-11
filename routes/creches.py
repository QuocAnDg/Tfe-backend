from flask import Blueprint, jsonify, request
from models import creches

bp_creches = Blueprint('creches', __name__)


@bp_creches.route('/<nom>', methods=['GET'])
def get_creche(nom):
    return jsonify(creches.read_une_creche(nom))


@bp_creches.route('/<nom>', methods=['POST'])
def modify_creche(nom):
    new_articles = request.json.get("articles", None)
    return jsonify(creches.modify_creche(nom, new_articles))