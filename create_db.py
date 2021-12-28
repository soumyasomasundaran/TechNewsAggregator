import mysql.connector as connector
connector = connector.connect(host="eu-cdbr-west-02.cleardb.net", user="b654141abcadfd", passwd="9b1b1f68")
cursor = connector.cursor()
query = "CREATE DATABASE heroku_75ce60fabbd29e1"
cursor.execute(query)
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)