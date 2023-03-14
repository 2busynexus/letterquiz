import mysql.connector as mysql
#from credentials import *

conn = mysql.connect(host="aws-eu-west-2.connect.psdb.cloud", 
                     database = "quizgamedb",
                     user = "kvhc9tqhx0g0b2ii9y2d", 
                     password = "pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs")
                
cursor = conn.cursor()

def connectionTest():
    if conn.is_connected():
        print(f"Connected to MySQL")
    else:
        print(f"Not connected")




