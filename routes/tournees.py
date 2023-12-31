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

    if len(tournees.read_tournee(nom_tournee)) != 0:
        return jsonify({"msg": "Erreur, il existe déjà une tournée avec ce nom"}), 406

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
        return jsonify({"msg": "Il n'existe pas de tournée avec ce nom"}), 404

    return jsonify(tournees.delete_tournee(nom))


@bp_tournees.route('/<nom>/editpreset', methods=['POST'])
@jwt_required()
def edit_preset_tournee(nom):
    
    liste_creches = request.json.get("crèches", None)

    tournee_found = tournees.read_tournee(nom)

    if len(tournee_found) == 0:
        return jsonify({"msg": "Il n'existe pas de tournée avec ce nom"}), 404
    
    tournees.delete_from_preset(nom)
    for creche in liste_creches:
        tournees.add_to_preset(nom, creche["nom"])
    
    
    return jsonify(creches.read_tous_les_creches_du_preset_dune_tournee(nom))

@bp_tournees.route('/<nom>/preset', methods=['GET'])
@jwt_required()
def read_preset_tournee(nom):
    return jsonify(creches.read_tous_les_creches_du_preset_dune_tournee(nom))


@bp_tournees.route('/<nom>/default', methods=['GET'])
@jwt_required()
def get_tournee_default(nom):
    return jsonify(tournees.read_une_tournee_defaut(nom))


@bp_tournees.route('/<nom>/replace', methods=['POST'])
@jwt_required()
def replace_nursery_tournee_(nom):
    
    liste_creches = request.json.get("crèches", None)

    tournees.delete_creche_tournee(nom)

    for creche in liste_creches:
        liste_article = {item["article"]["nom"]: item["quantite"] for item in creche["articleList"]}

        tournees.replace_creche_de_tournee(nom, creche["creche"]["nom"])
        creches.modify_creche(creche["creche"]["nom"], liste_article)

    return jsonify(tournees.read_une_tournee_defaut(nom))