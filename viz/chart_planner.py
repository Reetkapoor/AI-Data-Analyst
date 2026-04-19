import json
from google.genai import Client
import time
import os

client= Client(api_key= "AIzaSyDIMfW5NGHnFkMCxYYLsCk3xl0khx7GRBg")


def plan_visualization( question, df):
    columns = list(df.columns)

    prompt=f"""
You are a data visualization expert.

User Question:
{question}

Available columns:
{columns}

Choose the best visualization.

Return JSON ONLY in this format:

{{
 "chart_type": "bar | line | scatter | histogram | other | none",
 "x_axis": "column_name",
 "y_axis": "column_name",
 "reason": "short explanation"
}}
"""
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model =  "gemini-2.5-flash",
                contents = prompt
            )
            try: 
                plan = json.loads(response.text)
            except:
                plan = {"chart_type": "none"}

            return plan
        
        except Exception as e:
            print("Retrying due to:", str(e))
            time.sleep(5)

    raise Exception("Gemini API failed after retries")
