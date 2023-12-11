from flask import Blueprint, jsonify, request
from models import tournees
from models import creches

bp_tournees = Blueprint('tournees', __name__)


@bp_tournees.route('/', methods=['GET'])
def get_tournees():
    return jsonify(tournees.read_toutes_les_tournees())


@bp_tournees.route('/<tournee_id>', methods=['GET'])
def get_tournee(tournee_id):
    return jsonify(tournees.read_une_tournee(tournee_id))


@bp_tournees.route('/', methods=['POST'])
def add_tournee():
    nom_tournee = request.json.get("nom", None)
    liste_creches = request.json.get("crèches", None)

    tournee_found = tournees.read_tournee_from_nom(nom_tournee)

    if len(tournee_found) != 0:
        return jsonify({"msg": "Erreur, il existe déjà une tournée avec ce nom"}), 401

    tournees.creer_tournee(nom_tournee)
    for creche in liste_creches:
        creches.add_creche(creche["nom"], "Default", creche["articles"])
        tournees.ajouter_creche_a_tournee(nom_tournee, creche["nom"])

    return jsonify("ok")
