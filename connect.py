import sqlite3 as sql

conn = sql.connect("quizGame.db")

cursor = conn.cursor()