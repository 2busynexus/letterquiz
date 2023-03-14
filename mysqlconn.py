import mysql.connector as mysql
#from mysql.connector.constants import ClientFlag
#from credentials import *


config = {
    'user': 'kvhc9tqhx0g0b2ii9y2d',
    'password': 'pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs',
    'host': 'aws-eu-west-2.connect.psdb.cloud',
    'database': 'quizgamedb',
    'ssl_ca': "/etc/ssl/cert.pem",
    'use_pure': "True"
}

conn = mysql.connect(**config)
cursor = conn.cursor()

def connectionTest():
    if conn.is_connected():
        return print("Connected to MySQL")
    else:
        return print("Not connected")


