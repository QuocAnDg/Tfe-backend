from flask import Blueprint, jsonify, request
from models import articles
from flask_jwt_extended import jwt_required

bp_articles = Blueprint('articles', __name__)


@bp_articles.route('/', methods=['POST'])
@jwt_required()
def add_article():
    new_article = request.json.get("nom", None)
    if new_article is None or new_article == "":
        return jsonify({"msg": "Incorrect request"}), 400

    if len(articles.get_article(new_article)) != 0:
        return jsonify({"msg": "Article already existing"}), 406

    return jsonify(articles.add_article(new_article))


@bp_articles.route('/', methods=['GET'])
@jwt_required()
def get_articles():
    return jsonify(articles.read_tous_les_articles())


@bp_articles.route('/<nom>', methods=['DELETE'])
@jwt_required()
def delete_article(nom):
    if len(articles.get_article(nom)) == 0:
        return jsonify({"msg": "Article not present"}), 404
    return jsonify(articles.delete_article(nom))
