from utils import DBservice


def add_article(nom, unite):
    query = f"""CREATE (article:Article{{nom:"{nom}", unité:"{unite}"}}) RETURN article;"""
    return DBservice.runquery(query)


def get_article(nom):
    query = f"""MATCH (article:Article{{nom:"{nom}"}}) RETURN article;"""
    return DBservice.runquery(query)


def read_tous_les_articles():
    query = """MATCH (article:Article)
        RETURN article;"""
    return DBservice.runquery(query)


def delete_article(nom):
    query = f"""MATCH (a:Article{{nom: "{nom}"}})
        DELETE a;"""
    return DBservice.runquery(query)
