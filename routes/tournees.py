from flask import Blueprint, jsonify
from models import tournees

tournees_blueprint = Blueprint('tournees', __name__)


@tournees_blueprint.route('/', methods=['GET'])
def get_tournees():
    return jsonify(tournees.read_toutes_les_tournees())
