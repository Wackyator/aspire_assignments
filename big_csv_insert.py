from config import DBCreds

import csv
from uuid import uuid4

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def create_csv(row_count=20_000_000):
  """function to generate a file with size greater than 2GiB"""
  data = [[f"{uuid4()}", f"{uuid4()}", f"{uuid4()}", f"{uuid4()}"] for i in range(row_count)]
  with open("big_csv.csv", "a") as f:
    writer = csv.writer(f)
    for row in data:
      writer.writerow(row)

def main():
  cnx = create_engine(
    URL.create(
      drivername="mysql+pymysql",
      username=DBCreds.username, 
      password=DBCreds.passwd, 
      host=DBCreds.host, 
      port=DBCreds.port, 
      database=DBCreds.name
    ),
    echo = False
  )

  with pd.read_csv("./big_csv.csv", header=None, chunksize=10**7, iterator=True) as reader:
    i = 1
    for chunk in reader:
      chunk.to_sql("bulk_csv_insert_table", con=cnx)


if __name__ == "__main__":
  main()