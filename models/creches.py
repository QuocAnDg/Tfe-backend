from utils import DBservice


def read_une_creche(nom):
    query = f"""MATCH (creche:Creche {{nom : "{nom}"}})-[c:CONTIENT]->(article:Article)
        WITH creche, COLLECT({{article: article, quantite: c.quantite}}) AS articleList
        RETURN creche, articleList;"""

    return DBservice.runquery(query)