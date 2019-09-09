import sqlite3 as lite
import pandas as pd
import boto3


bucket = "demo-for-ds"
file_name = "data/Churn_Modelling.csv"


def read_from_s3(bucket, file_name):

    s3 = boto3.client('s3')
    # 's3' is a key word. create connection to S3 using default config and all
    # buckets within S3

    obj = s3.get_object(Bucket=bucket, Key=file_name)
    # get object and file (key) from bucket

    df = pd.read_csv(obj['Body'])  # 'Body' is a key word
    print(df.head())


# read_from_s3(bucket, file_name)

# SQL

def create_db_with_data():
    con = lite.connect('population.db')

    with con:
        cur = con.cursor()
        # each excution create a new column and called record
        cur.execute(
            "CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT)")
        cur.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537)")
        cur.execute("INSERT INTO Population VALUES(NULL,'France', 66415161)")
        cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
        cur.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612)")
        cur.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")

def query_from_db():
    conn = lite.connect('population.db')
    query = "SELECT country FROM Population WHERE population > 50000000;"
    # query = "SELECT country FROM Population WHERE country LIKE 'S%'"

    df = pd.read_sql_query(query, conn)

    for country in df['country']:
        print(country)

# querying
query_from_db()
