import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            user="Harika",
            password="smarthealthpvt",
            host="localhost",
            port="5432",
            database="harika_db"
        )
        print("Successfully connected to PostgreSQL!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

if __name__ == "__main__":
    print("Attempting to connect to PostgreSQL...")
    conn = get_db_connection()
    if conn is not None:
        print("Connection successful!")
        conn.close()
    else:
        print("Failed to connect to PostgreSQL.")


