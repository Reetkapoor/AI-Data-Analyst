def load_schema_chunks(schema_path = "data\schema_context.txt"):
    
    with open(schema_path, 'r') as f:
        schema_text = f.read()
    
    tables = schema_text.split("Table:")

    chunks = []

    for table in tables:
        table = table.strip()

        if not table:
            continue

        chunk = "Table: " + table

        chunks.append(chunk)

    return chunks