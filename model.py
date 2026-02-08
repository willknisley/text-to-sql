client = OpenAI()
import sqlite3

conn = sqlite3.connect("rental.db")
cursor = conn.cursor()

def get_response():
    user_question = input("What would you like to ask about the database?")
    prompt = f"Convert this question into SQL for a car rental database: {user_question} and only return SQL."

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )
    
    query = response.output_text.strip()
    print(query)