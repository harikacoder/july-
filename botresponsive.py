# botresponsive.py
import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None


def get_pdf_location(employee_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT pdf_location
        FROM Employees
        WHERE employee_name = %s
    """, (employee_name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def chat():
    print("Chatbot: Hi there! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            pdf_location = get_pdf_location(user_input)
            if pdf_location:
                print(f"Chatbot: Here is the PDF location for {user_input}: {pdf_location}")
            else:
                print("Chatbot: Employee not found or PDF location not available.")

if __name__ == '__main__':
    chat()
