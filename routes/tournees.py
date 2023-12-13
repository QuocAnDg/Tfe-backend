from flask import Blueprint, jsonify, request
from models import tournees
from models import creches
from flask_jwt_extended import jwt_required

bp_tournees = Blueprint('tournees', __name__)


@bp_tournees.route('/', methods=['GET'])
@jwt_required()
def get_tournees():
    return jsonify(tournees.read_toutes_les_tournees())


@bp_tournees.route('/<nom>', methods=['GET'])
@jwt_required()
def get_tournee(nom):
    return jsonify(tournees.read_une_tournee(nom))


@bp_tournees.route('/', methods=['POST'])
@jwt_required()
def add_tournee():
    nom_tournee = request.json.get("nom", None)
    liste_creches = request.json.get("crèches", None)

    tournee_found = tournees.read_tournee(nom_tournee)

    if len(tournee_found) != 0:
        return jsonify({"msg": "Erreur, il existe déjà une tournée avec ce nom"}), 401

    tournee_cree = tournees.creer_tournee(nom_tournee)
    for creche in liste_creches:
        creches.add_creche(creche["nom"], creche["adresse"], creche["telephone"], creche["articles"])
        tournees.ajouter_creche_a_tournee(nom_tournee, creche["nom"])

    return jsonify(tournee_cree)


@bp_tournees.route('/<nom>', methods=['DELETE'])
@jwt_required()
def delete_tournee(nom):
    tournee_found = tournees.read_tournee(nom)

    if len(tournee_found) == 0:
        return jsonify({"msg": "Erreur, il n'existe pas de tournée avec ce nom"}), 401

    return jsonify(tournees.delete_tournee(nom))
