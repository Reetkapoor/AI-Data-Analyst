from google.genai import Client
import time
import os

client= Client(api_key= "AIzaSyCLgj-uu65fgdyV3jqyoTvQ-1WvB7dE34k")

def generate_out_of_scope_response(question):

    prompt = f"""
You are an AI data analyst assistant.

The user asked: "{question}"

This question is not related to querying the database.

Respond politely and guide the user to ask questions about the database.
Give examples of data-related questions they can ask.

Keep the response short and helpful.
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

def is_data_question(question):
    prompt = f"""
You are a strict classifier.

A query is a DATA QUESTION only if it clearly asks about:
- tables
- records
- numbers
- statistics
- sales
- counts
- database information

If the query is not CLEARLY asking about database information, return NO

Examples:

User: "How many orders were placed last month?"
Answer: YES

User: "Show total sales by region"
Answer: YES

User: "Hello"
Answer: NO

User: "How are you?"
Answer: NO

User: "Tell me a joke"
Answer: NO

Now classify the query.

Respond with ONLY YES or NO.

Query: {question}
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


