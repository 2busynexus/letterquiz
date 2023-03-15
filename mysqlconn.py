import mysql.connector as mysql
#from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

#PLANET SCALE INSTRUCTIONS

"""import MySQLdb as mysql

conn = mysql.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)"""


#MYSQL.CONNECTOR SETTINGS

"""conn = mysql.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  port=3306,
  ssl_verify_cert = False,
  ssl_ca = "/etc/ssl/cert.pem"
)"""


#LOCALHOST
conn = mysql.connect(
    user= 'root',
    password= os.getenv('password2'),
    host= 'localhost',
    database= 'quizgamedb',

)

#PYTHON ANYWHERE DB

conn = mysql.connect(
  host= "iammihai.mysql.pythonanywhere-services.com",
  user= "iammihai",
  passwd= "quizgame",
  db= "iammihai$letterquiz",
  ssl_verify_cert = False,
  ssl_ca = "/etc/ssl/cert.pem"
)

cursor = conn.cursor()


def connectionTest():
    if conn.is_connected():
        return print("Connected to MySQL")
    else:
        return print("Not connected")

connectionTest()



