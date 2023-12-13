from utils import DBservice
import bcrypt


def readoneuserfromusername(username):
    query = f"""MATCH (user:User {{username: "{username}"}}) RETURN user"""
    return DBservice.runquery(query)


def createOne(username, password):
    hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    query = f"""CREATE (user:User {{username:"{username}",password:"{hashed_password}", isAdmin:false}}) RETURN user;"""
    return DBservice.runquery(query)

def login(username, plain_text_password):
    user_found = readoneuserfromusername(username)
    return len(user_found) != 0 and bcrypt.checkpw(bytes(plain_text_password, 'utf-8'),bytes(user_found[0]["user"]["password"][1:].replace("'", ""), 'utf-8'))
