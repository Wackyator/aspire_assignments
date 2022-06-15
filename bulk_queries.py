from config import DBCreds

from uuid import uuid4

import mysql.connector

def get_db(creds):
  db = mysql.connector.connect(
    host = creds.host,
    port = creds.port,
    user = creds.username,
    passwd = creds.passwd,
    database = creds.name,
  )
  return db

def create_table(cursor):
  """function to create the table for bulk inserts"""
  query = "CREATE TABLE bulk_queries_table (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, field1 varchar(50) NOT NULL)"

  cursor.execute(query)

def bulk_insert(cursor):
  """function doing performing the bulk inserts"""
  query = "INSERT INTO bulk_queries_table (field1) VALUES (%s)"
  data = [(f"{uuid4()}",) for i in range(2000)]

  cursor.executemany(query, data)

def main():
  db = get_db(DBCreds)
  cur = db.cursor()
  create_table(cur)
  bulk_insert(cur)
  db.commit()
  cur.execute("SELECT * FROM bulk_queries_table")
  cur.fetchall()
  print(cur.rowcount)
  # cur.execute("DROP TABLE User")
  # db.commit()
  
if __name__ == "__main__":
  main()