from utils import DBservice


def read_toutes_les_tournees():
    query = """MATCH (tournee:Tournee)
        RETURN tournee;"""
    return DBservice.runquery(query)


def read_une_tournee(nom):
    query = f"""MATCH (tournee:Tournee{{nom:"{nom}"}})-[:LIVRE]->(creche:Creche)-[c:CONTIENT]->(article:Article)
        WITH creche, COLLECT({{article: article, quantite: c.quantite}}) AS articleList
        RETURN creche,articleList;"""
    return DBservice.runquery(query)


def read_tournee(nom):
    query = f"""MATCH (tournee:Tournee {{nom: "{nom}"}})
        RETURN tournee;"""
    return DBservice.runquery(query)


def creer_tournee(nom):
    query = f"""CREATE (t:Tournee{{nom:"{nom}"}});"""
    return DBservice.runquery(query)


def delete_tournee(nom):
    # TODO: supprimer les relations de la node, les creches et les relations entre creche et article
    query = f"""MATCH (tournee:Tournee{{nom:"{nom}"}}) DELETE TOURNEE;"""
    return DBservice.runquery(query)


def ajouter_creche_a_tournee(nom_tournee, nom_creche):
    query=f"""MATCH (t:Tournee {{nom:"{nom_tournee}"}}), (c:Creche {{nom:"{nom_creche}"}})
    CREATE (t)-[:LIVRE]->(c);"""
    return DBservice.runquery(query)
