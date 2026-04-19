from core.llm_sql import generate_sql, explain_result
import psycopg2 
import pandas as pd

def run_sql(query):

    conn = psycopg2.connect(
        host="localhost",
        database="adventureworks",
        user="postgres",
        password="reet",
        port="6138"
    )

    try:

        df = pd.read_sql_query(query, conn)
        conn.close()

        return df, None

    except Exception as e:

        conn.close()

        return None, str(e)


