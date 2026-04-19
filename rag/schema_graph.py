import psycopg2

def get_foreign_keys():

    conn = psycopg2.connect(
        host = 'localhost',
        database = 'adventureworks',
        user = 'postgres',
        password = 'reet',
        port = '6138'
    )

    cursor = conn.cursor()

    query = '''
    SELECT
    tc.table_schema,
    tc.table_name,
    ccu.table_schema AS foreign_table_schema, 
    ccu.table_name AS foreign_table_name 
    FROM information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu 
    ON tc.constraint_name = kcu.constraint_name 
    JOIN information_schema.constraint_column_usage AS ccu 
    ON ccu.constraint_name = tc.constraint_name 
    WHERE tc.constraint_type = 'FOREIGN KEY';
    '''

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    fk_graph = {}

    for row in rows:
        table = f"{row[0]}.{row[1]}"
        foreign_table = f"{row[2]}.{row[3]}"

        if table not in fk_graph:
            fk_graph[table] = []

        fk_graph[table].append(foreign_table)
    
    return fk_graph

