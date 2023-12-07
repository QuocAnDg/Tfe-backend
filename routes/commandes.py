from flask import Blueprint, jsonify
from models import commandes


commandes_blueprint = Blueprint('commandes', __name__)


@commandes_blueprint.route('/<tourneeid>', methods=['GET'])
def get_commandes_tournee(tourneeid):
    return jsonify(commandes.read_commandes_dune_tournee(tourneeid))