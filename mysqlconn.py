import mysql.connector as mysql
from mysql.connector import Error
from dotenv import load_dotenv
import os


load_dotenv()

conn = mysql.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  #ssl_mode = "VERIFY_IDENTITY",
  ssl_verify_cert = True,
  ssl_ca = "/etc/ssl/cert.pem"
 
)

#config = {
  #  'user': 'kvhc9tqhx0g0b2ii9y2d',
 #   'password': 'pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs',
  #  'host': 'aws-eu-west-2.connect.psdb.cloud',
  #  'database': 'quizgamedb',
  #  'ssl_ca': "/etc/ssl/cert.pem",  # path to the CA certificate
  #  'ssl_cert': 'etc/ssl/server-cert.pem',  # path to the client certificate
  #  'ssl_key': 'etc/ssl/server-key.pem',  # path to the client private key

#}

#ionos
"""conn = mysql.connect(
    user= 'kvhc9tqhx0g0b2ii9y2d',
    password= 'pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs',
    host= 'aws-eu-west-2.connect.psdb.cloud',
    database= 'quizgamedb',

)"""

cursor = conn.cursor()


#conn = mysql.connect(**config)
#cursor = conn.cursor()

def connectionTest():
    if conn.is_connected():
        return print("Connected to MySQL")
    else:
        return print("Not connected")

connectionTest()

"""try:
    if conn.is_connected():
        tryCursor = conn.cursor()
    cursor.execute("select @@version ")
    version = cursor.fetchone()
    if version:
        print('Running version: ', version)
    else:
        print('Not connected')
except Error as e:
    print("error while connecting", e)
finally:
    conn.close()"""


