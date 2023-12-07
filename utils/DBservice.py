from flask import jsonify
from neo4j import GraphDatabase
import os

# Neo4j configuration
uri = os.getenv('DB_URI')
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(db_username, db_password))


def runquery(query):
    with driver.session() as session:
        nodes = session.run(query).data()
    return nodes
