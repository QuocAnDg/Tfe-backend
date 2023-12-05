from flask import Flask, jsonify, request
from flask_cors import CORS
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

# Neo4j configuration
uri = os.getenv('DB_URI')
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(username, password))


@app.get('/users')
def get_users():
    query = "MATCH (n:User) RETURN n"
    with driver.session() as session:
        nodes = session.run(query).data()
    return jsonify(nodes)


@app.get('/commandes')
def get_commandes():
    query = "MATCH (n:Commande) RETURN n"
    with driver.session() as session:
        nodes = session.run(query).data()
    return jsonify(nodes)


if __name__ == '__main__':
    app.run(debug=True)
