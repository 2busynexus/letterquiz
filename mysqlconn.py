import mysql.connector as mysql
#from credentials import *

conn = mysql.connect(host="aws-eu-west-2.connect.psdb.cloud", 
                     database = "quizgamedb",
                     user = "kvhc9tqhx0g0b2ii9y2d", 
                     password = "pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs")

connection_uri = (
    "mysql+mysqldb://scott:tiger@192.168.0.134/test"
    "?ssl_ca=/home/gord/client-ssl/ca.pem"
    "&ssl_cert=/home/gord/client-ssl/client-cert.pem"
    "&ssl_key=/home/gord/client-ssl/client-key.pem"
)

cursor = conn.cursor()

def connectionTest():
    if conn.is_connected():
        return print("Connected to MySQL")
    else:
        return print("Not connected")




