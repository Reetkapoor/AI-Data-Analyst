import psycopg2


def get_schema_for_tables(tables):

    conn = psycopg2.connect(
        host="localhost",
        database="adventureworks",
        user="postgres",
        password="reet",
        port = "6138"
    )

    cursor = conn.cursor()

    schema_text = ""

    for table in tables:

        schema, table_name = table.split(".")

        query = """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = %s
        AND table_name = %s
        ORDER BY ordinal_position
        """

        cursor.execute(query, (schema, table_name))
        columns = cursor.fetchall()

        schema_text += f"Table: {table}\n"
        schema_text += "Columns:\n"

        for col in columns:
            schema_text += f"- {col[0]}\n"

        schema_text += "\n"

    cursor.close()
    conn.close()

    return schema_text