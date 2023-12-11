from utils import DBservice


def readoneuserfromusername(username):
    query = f"""MATCH (user:User {{username: "{username}"}}) RETURN user"""
    return DBservice.runquery(query)


def createOne(username, password):
    query = f"""CREATE (user:User {{username:"{username}",password:"{password}", isAdmin:false}}) RETURN user;"""
    return DBservice.runquery(query)


