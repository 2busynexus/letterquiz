from mysqlconn import *
#from database import *

"""def showTables():
    cursor.execute("SHOW TABLES")
    tables = []
    for table in cursor:
        tables.append(table)
    return tables"""

def countriesRows(str):
    cursor.execute(f"SELECT * FROM countries WHERE country LIKE '{str}%' ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[1])
    conn.close()
    return data

#print(countriesRows("a"))

def citiesRows(str):
    cursor.execute(f"SELECT * FROM cities WHERE city LIKE '{str}%' ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[1])
    conn.close()
    return data

def watersRows(str):
    cursor.execute(f"SELECT * FROM water_country WHERE water LIKE '{str}%' ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[1])
    conn.close()
    return data

def mountainsRows(str):
    cursor.execute(f"SELECT * FROM mountain_country WHERE mountain LIKE '{str}%' ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[1])
    conn.close()
    return data

def cropsRows(str):
    cursor.execute(f"SELECT * FROM crops WHERE crop LIKE '{str}%' ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[1])
    conn.close()
    return data

def animalsRows(str):
    cursor.execute(f"SELECT * FROM animals WHERE animal LIKE '{str}%' ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[1])
    conn.close()
    return data

def allRows(answer, data):
    lowerDAta = [x.lower() for x in data]
    if answer.lower() in lowerDAta:
        return 10
    else:
        return 0
