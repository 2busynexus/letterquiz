from mysqlconn import *
#from database import *

class user():
    id = ""
    userName = ""
    email = ""
    password = ""
    highScore = ""

def newUser(username, email, password):
    #query to add in users table
    cursor.execute(f"INSERT INTO userProfile (userName, email, password) VALUES ('{username}', '{email}', '{password}')")
    conn.commit()

def checkUser(username, email):
    cursor.execute(f"SELECT * FROM userProfile WHERE username = '{username}' OR email = '{email}'")
    profile = cursor.fetchall()
    return profile
    #query to look for user in the table

def updateUser(key, value, username):

    if key=="email":
        cursor.execute(f"SELECT * FROM userProfile WHERE email ='{value}'")
        check = cursor.fetchall()
        if check:
            print("emails is already assigned to someone else")
            return False
        else:
            cursor.execute(f"UPDATE userProfile SET email = '{value}' WHERE username = '{username}'")
            conn.commit()
            return True

    if key=="password":
        cursor.execute(f"UPDATE userProfile SET password='{value}' WHERE username = '{username}'")
        conn.commit()

def deleteUser(username):
    cursor.execute(f"DELETE FROM userProfile WHERE username = '{username}'")
    conn.commit()

def addHighscore(points, username):
    cursor.execute(f"UPDATE userProfile SET highscore = highscore+{points} WHERE username = '{username}'")
    conn.commit()

    
   
def checkHighscore(username):
    cursor.execute(f"SELECT highscore FROM userProfile WHERE username ='{username}'")
    highscore = cursor.fetchone()
    return highscore

def score(answers):
    points = 0
    for i in answers.values():
        points+=i
    return points
 
