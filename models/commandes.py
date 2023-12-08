from utils import DBservice


def read_commandes_dune_tournee(tourneeid):
    query = f"""MATCH (tournee:Tournee)-[:POSSEDE]->(commande:Commande)
        WHERE tournee.ordre = {tourneeid}
        RETURN commande;"""
    return DBservice.runquery(query)
