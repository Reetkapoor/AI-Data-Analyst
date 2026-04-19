from google.genai import Client
import time

client= Client(api_key= "AIzaSyCLgj-uu65fgdyV3jqyoTvQ-1WvB7dE34k")

def fix_sql( sql, error, schema_context):

    prompt = f"""
You are a PostgreSQL expert.

The following SQL query failed.

SQL:
{sql}

Database Error:
{error}

Schema_context :
{schema_context}

Fix the SQL query so that it runs correctly.

Rules:
- Only return SQL
- Do not explain anything
- Ensure it works in PostgreSQL
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