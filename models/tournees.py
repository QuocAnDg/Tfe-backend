from utils import DBservice


def read_toutes_les_tournees():
    query = """MATCH (tournee:Tournee)
        RETURN tournee;"""
    return DBservice.runquery(query)


def read_une_tournee(nom):
    query = f"""MATCH (tournee:Tournee{{nom:"{nom}"}})-[:LIVRE]->(creche:Creche)-[c:CONTIENT]->(article:Article)
        WITH creche, COLLECT({{article: article, quantite: c.quantite, unité:c.unité}}) AS articleList
        RETURN creche,articleList;"""
    return DBservice.runquery(query)


def read_tournee(nom):
    query = f"""MATCH (tournee:Tournee {{nom: "{nom}"}})
        RETURN tournee;"""
    return DBservice.runquery(query)


def creer_tournee(nom):
    query = f"""CREATE (t:Tournee{{nom:"{nom}"}}) RETURN t;"""
    return DBservice.runquery(query)


def delete_tournee(nom):
    query = f"""MATCH (t:Tournee {{nom: "{nom}"}})-[r:LIVRE]->(c:Creche)-[r2:CONTIENT]->(a:Article)
    DETACH DELETE t, r, c, r2;"""
    return DBservice.runquery(query)


def ajouter_creche_a_tournee(nom_tournee, nom_creche):
    query=f"""MATCH (t:Tournee {{nom:"{nom_tournee}"}}), (c:Creche {{nom:"{nom_creche}"}})
    CREATE (t)-[:LIVRE]->(c)
    CREATE (t)-[:LIVRE_PAR_DEFAUT]->(c)
    ;"""
    return DBservice.runquery(query)


def delete_from_preset(nom_tournee):
    query=f"""MATCH (t:Tournee {{nom:"{nom_tournee}"}})-[r:LIVRE_PAR_DEFAUT]->(c:Creche)
    DETACH DELETE r;"""
    return DBservice.runquery(query)

def add_to_preset(nom_tournee, nom_creche):
    query=f"""MATCH (t:Tournee {{nom:"{nom_tournee}"}}), (c:Creche {{nom:"{nom_creche}"}})
    CREATE (t)-[:LIVRE_PAR_DEFAUT]->(c);"""
    return DBservice.runquery(query)


def read_une_tournee_defaut(nom):
    query = f"""MATCH (tournee:Tournee{{nom:"{nom}"}})-[:LIVRE_PAR_DEFAUT]->(creche:Creche)-[c:CONTIENT_PAR_DEFAUT]->(article:Article)
        WITH creche, COLLECT({{article: article, quantite: c.quantite_par_defaut, unité:c.unité}}) AS articleList
        RETURN creche,articleList;"""
    return DBservice.runquery(query)

def delete_creche_tournee(nom_tournee):
    query=f"""MATCH (t:Tournee {{nom:"{nom_tournee}"}})-[r:LIVRE]->(c:Creche)
    DETACH DELETE r;"""
    return DBservice.runquery(query)

def replace_creche_de_tournee(nom_tournee, nom_creche):
    query=f"""MATCH (t:Tournee {{nom:"{nom_tournee}"}}), (c:Creche {{nom:"{nom_creche}"}})
    CREATE (t)-[:LIVRE]->(c)
    ;"""
    return DBservice.runquery(query)