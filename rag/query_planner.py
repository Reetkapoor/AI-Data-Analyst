from google.genai import Client
import time
import os

client= Client(api_key= "AIzaSyCLgj-uu65fgdyV3jqyoTvQ-1WvB7dE34k")

def generate_query_plan(question, schema_context):

    prompt = f"""
You are a database expert.

Given a user question and database schema,
create a step-by-step plan to answer the question.

Do NOT write SQL.

Explain which tables, joins, and aggregations are needed.

Schema:
{schema_context}

Question:
{question}

Query Plan:
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