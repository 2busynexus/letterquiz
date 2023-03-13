from rows import *
from dataHandle import *

letters = 'abcdefghijklmnopqrstuvwxyz'


def checkSignUp(username, email, password):
    profile = checkUser(username, email)
    #print(profile)
    if not profile:
        newUser(username, email, password)
        return True
    else:
        return False

    #check if users exists - if not, add user to table
    #if user is created ok return true

def checkLogin(username, password):
    profile = checkUser(username, username)
    if not profile:
        return False
    if password == profile[0][3]:
        return True
    else:
        return False
    
    #check if user exists in table, if yes return True, if not then refresh page with error

#def userProfile():
    #cursor.execute(f"SELECT * FROM users WHERE username = {str} & ")

def checkEmail(email):
    cursor.execute(f"SELECT * FROM userProfile WHERE email = {email}")
    results = cursor.fetchall()
    if results:
        print("EXISTS")
    else:
        print("NOT EXIST")

def getProfile(user):
    cursor.execute(f"SELECT * FROM userProfile WHERE username = '{user}'")
    profile = cursor.fetchall()
    return(profile)