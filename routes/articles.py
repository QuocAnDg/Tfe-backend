from flask import Blueprint, jsonify, request
from models import articles

bp_articles = Blueprint('articles', __name__)


@bp_articles.route('/', methods=['POST'])
def add_article():
    new_article = request.json.get("nom", None)
    return jsonify(articles.add_article(new_article))