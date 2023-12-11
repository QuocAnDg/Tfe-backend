from utils import DBservice


def read_toutes_les_tournees():
    query = """MATCH (tournee:Tournee)
        RETURN tournee;"""
    return DBservice.runquery(query)


def read_une_tournee(tourneeid):
    query = f"""MATCH (tournee:Tournee)-[:LIVRE]->(creche:Creche)-[c:CONTIENT]->(article:Article)
        WHERE tournee.id = {tourneeid}
        WITH creche, COLLECT({{article: article, quantite: c.quantite}}) AS articleList
        RETURN creche,articleList;"""
    return DBservice.runquery(query)


def read_tournee_from_nom(nom):
    query = f"""MATCH (tournee:Tournee {{nom: "{nom}"}})
        RETURN tournee;"""
    return DBservice.runquery(query)


def creer_tournee(nom):
    query = f"""CREATE (t:Tournee{{nom:"{nom}"}});"""
    return DBservice.runquery(query)
