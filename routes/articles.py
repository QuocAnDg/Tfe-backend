from flask import Blueprint, jsonify, request
from models import articles
from flask_jwt_extended import jwt_required

bp_articles = Blueprint('articles', __name__)


@bp_articles.route('/', methods=['POST'])
@jwt_required()
def add_article():
    new_article = request.json.get("nom", None)
    return jsonify(articles.add_article(new_article))


@bp_articles.route('/', methods=['GET'])
@jwt_required()
def get_articles():
    return jsonify(articles.read_tous_les_articles())


@bp_articles.route('/<nom>', methods=['DELETE'])
@jwt_required()
def delete_article(nom):
    return jsonify(articles.add_article(nom))
