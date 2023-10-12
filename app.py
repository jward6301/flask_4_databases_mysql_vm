import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect
from flask import Flask, render_template
import pandas as pd


load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


def get_tables(engine):
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    return read_sql(query, engine)


# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM medications" 
df = execute_query_to_dataframe(sql_query, db_engine)

sql_query2 = "SELECT * FROM patients" 
df2 = execute_query_to_dataframe(sql_query2, db_engine)

sql_query3 = "SELECT * FROM patient_medications" 
df3 = execute_query_to_dataframe(sql_query3, db_engine)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/database')
def database(database=df, database2=df2, database3=df3):
    return render_template('database.html', database=database, database2=database2, database3=database3)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )