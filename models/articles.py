from utils import DBservice


def add_article(nom):
    query = f"""CREATE (article:Article{{nom:"{nom}"}}) RETURN article;"""
    DBservice.runquery(query)


def read_tous_les_articles():
    query = """MATCH (article:Article)
        RETURN article;"""
    return DBservice.runquery(query)
