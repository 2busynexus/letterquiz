"""import mysql.connector as mysql
#from mysql.connector.constants import ClientFlag
#from credentials import *


config = {
    'user': 'kvhc9tqhx0g0b2ii9y2d',
    'password': 'pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs',
    'host': 'aws-eu-west-2.connect.psdb.cloud',
    'database': 'quizgamedb',
    'ssl_ca': "/etc/ssl/cert.pem",  # path to the CA certificate
    'ssl_cert': 'etc/ssl/server-cert.pem',  # path to the client certificate
    'ssl_key': 'etc/ssl/server-key.pem',  # path to the client private key

}

conn = mysql.connect(**config)
cursor = conn.cursor()

def connectionTest():
    if conn.is_connected():
        return print("Connected to MySQL")
    else:
        return print("Not connected")


"""