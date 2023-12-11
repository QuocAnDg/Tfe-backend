from utils import DBservice


def read_une_creche(nom):
    query = f"""MATCH (creche:Creche {{nom : "{nom}"}})-[c:CONTIENT]->(article:Article)
        WITH creche, COLLECT({{article: article, quantite: c.quantite}}) AS articleList
        RETURN creche, articleList;"""

    return DBservice.runquery(query)


def add_creche(nom, adresse, articles):
    query = f"""CREATE (c:Creche{{nom:"{nom}", adresse: "{adresse}"}});"""
    DBservice.runquery(query)

    for article in articles.keys():
        query = f"""MATCH (c:Creche {{nom:"{nom}"}}), (a:Article {{nom:"{article}"}})
            CREATE (c)-[:CONTIENT {{quantite:{articles[article]}}}]->(a);"""
        DBservice.runquery(query)


def modify_creche(nom, new_articles):
    delete_query = f"""MATCH (c:Creche{{nom: "{nom}"}})-[contient:CONTIENT]->(a:Article)
    DELETE contient;"""
    DBservice.runquery(delete_query)

    for article in new_articles.keys():
        query = f"""MATCH (c:Creche {{nom:"{nom}"}}), (a:Article {{nom:"{article}"}})
            CREATE (c)-[:CONTIENT {{quantite:{new_articles[article]}}}]->(a);"""
        DBservice.runquery(query)
