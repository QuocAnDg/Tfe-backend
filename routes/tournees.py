from flask import Blueprint, jsonify, request
from models import tournees

bp_tournees = Blueprint('tournees', __name__)


@bp_tournees.route('/', methods=['GET'])
def get_tournees():
    return jsonify(tournees.read_toutes_les_tournees())


@bp_tournees.route('/', methods=['POST'])
def add_tournee():
    nom_tournee = request.json.get("nom", None)

    tournee_found = tournees.read_tournee_from_nom(nom_tournee)

    if len(tournee_found) != 0:
        return jsonify({"msg": "Erreur, il existe déjà une tournée avec ce nom"}), 401

    tournees.creer_tournee(nom_tournee)
    return jsonify()
