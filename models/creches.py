from utils import DBservice


def read_une_creche(nom):
    query = f"""MATCH (creche:Creche {{nom : "{nom}"}})
        RETURN creche;"""
    return DBservice.runquery(query)