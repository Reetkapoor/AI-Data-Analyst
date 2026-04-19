from .retriever import retrieve_relevant_schema
from .schema_graph import get_foreign_keys

def expand_schema_tables(tables):

    expanded_tables = set(tables)
    fk_graph = get_foreign_keys()

    for table in tables:

        if table in fk_graph:

            for connected_table in fk_graph[table]:
                expanded_tables.add(connected_table)

    return list(expanded_tables)

def get_schema_context(question):

    retrieved_tables = retrieve_relevant_schema(question)

    table_names=[]

    for chunk in retrieved_tables:
        line = chunk.split("\n")[0]

        table_name = line.replace("Table:", "").strip()

        table_names.append(table_name)

    expanded_tables = expand_schema_tables(table_names)

    return expanded_tables
