import mysql.connector as connector
connector = connector.connect(host="localhost", user="root", passwd="Minimum$15")
cursor = connector.cursor()
query = "CREATE DATABASE technews"
cursor.execute(query)
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)