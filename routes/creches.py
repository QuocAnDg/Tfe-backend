from flask import Blueprint, jsonify
from models import creches

bp_creches = Blueprint('creches', __name__)


@bp_creches.route('/<nom>', methods=['GET'])
def get_creche(nom):
    return jsonify(creches.read_une_creche(nom))