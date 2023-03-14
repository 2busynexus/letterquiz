from mysqlconn import *
"""#from database import *

class user():
    id = ""
    userName = ""
    email = ""
    password = ""
    highScore = ""

def newUser(username, email, password):
    #query to add in users table
    #cursor.execute(f"INSERT INTO userProfile (userName, email, password) VALUES ('{username}', '{email}', '{password}')")
    #conn.commit()
    conn = engine.connect()
    query = text("INSERT INTO userProfile (userName, email, password) VALUES (:username, :email, :password)")
    values = {"username": username, "email": email, "password": password}
    conn.execute(query, values)
    conn.close()
"""
def checkUser(username, email):
    cursor.execute(f"SELECT * FROM userProfile WHERE username = '{username}' OR email = '{email}'")
    profile = cursor.fetchall()
    return profile
    #query to look for user in the table
"""
def updateUser(key, value, username):
    conn = engine.connect()
    if key=="email":
        query = text("SELECT * FROM userProfile WHERE email = :value")
        check = conn.execute(query, value=value).fetchall()
        if check:
            print("emails is already assigned to someone else")
            return False
        else:
            query = text("UPDATE userProfile SET email = :value WHERE username = :username")
            conn.execute(query, value=value, username=username)
            return True

    if key == "password":
        query = text("UPDATE userProfile SET password=:value WHERE username=:username")
        conn.execute(query, value=value, username=username)
        conn.commit()

    conn.close()


def deleteUser(username):
    conn = engine.connect()
    query = text("DELETE FROM userProfile WHERE username = :username")
    conn.execute(query, username=username)
    conn.close()

def addHighscore(points, username):
    conn = engine.connect()
    query = text("UPDATE userProfile SET highscore = highscore+ :points WHERE username = :username")
    conn.execute(query, points=points, username=username)
    conn.close()

    
def checkHighscore(username):
    conn = engine.connect()
    query = text("SELECT highscore FROM userProfile WHERE username = :username")
    highscore = conn.execute(query, username=username).fetchone()
    conn.close()
    return highscore

def score(answers):
    points = 0
    for i in answers.values():
        points+=i
    return points
 
"""