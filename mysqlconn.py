import mysql.connector as mysql
from credentials import *

conn = mysql.connect(host="localhost", 
                     database = "quizGameDB",
                     user = "root", 
                     password = passwd)
                
cursor = conn.cursor()

def connectionTest():
    if conn.is_connected():
        print(f"Connected to MySQL")
    else:
        return(f"Not connected")




