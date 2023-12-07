from utils import DBservice


def readoneuserfromusername(username):
    query = f"""MATCH (user:User {{username: "{username}"}}) RETURN user"""
    return DBservice.runquery(query)


