from utils import DBservice


def add_article(nom):
    query = f"""CREATE (article:Article{{nom:"{nom}"}}) RETURN article;"""
    DBservice.runquery(query)

