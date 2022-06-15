from config import DBCreds

import mysql.connector

db = mysql.connector.connect(
  host = DBCreds.host,
  port = DBCreds.port,
  user = DBCreds.username,
  passwd = DBCreds.passwd,
  database = DBCreds.name,
)

cur = db.cursor()
cur.execute("SELECT CURTIME()")
print(cur.fetchone())