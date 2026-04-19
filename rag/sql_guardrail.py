import re

def clean_sql(sql):
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()

def validate_sql(sql):
    sql = clean_sql(sql)
    if not sql.strip():
        raise ValueError("Generated SQL is empty")
    
    if not sql.lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed")
    
    forbidden = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create"
    ]

    for word in forbidden:
        if re.search(rf"\b{word}\b", sql.lower()):
            raise ValueError(f"Forbidden SQL operation detected: {word}")
        
    return sql