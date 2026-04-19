from google.genai import Client
import time
import os
from rag.query_planner import generate_query_plan

client= Client(api_key= "AIzaSyCLgj-uu65fgdyV3jqyoTvQ-1WvB7dE34k")

    
def generate_sql(question, schema_context):
    query_plan = generate_query_plan(question, schema_context)
    prompt = f"""
You are an expert SQL generator.
The database is PostgreSQL.

Use the following database schema to answer the question.

{schema_context}

Use the following query plan, to generate the query

{query_plan}

Instructions:
- Generate a valid SQL query.
- Use PostgreSQL syntax only.
- Use only the tables and columns provided.
- Use proper joins when necessary.
- Return only SQL, no explanation.

User Question:
{question}
"""
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model =  "gemini-2.5-flash",
                contents = prompt
            )

            return  response.text.strip()
        
        except Exception as e:
            print("Retrying due to:", str(e))
            time.sleep(5)

    raise Exception("Gemini API failed after retries")

def explain_result(question, result):

    prompt = f"""
User Question: {question}

Database Result: {result}

Read the dataframe and explain the result in one simple sentence.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model =  "gemini-2.5-flash",
                contents = prompt
            )

            return  response.text.strip()
        
        except Exception as e:
            print("Retrying due to:", str(e))
            time.sleep(5)

    raise Exception("Gemini API failed after retries")

