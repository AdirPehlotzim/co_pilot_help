import os
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), "mydatabase.db")

def create_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT,
        profile_picture TEXT,
        admin INTEGER DEFAULT 0
    );
    """)

    conn.commit()
    conn.close()
    print("Database created successfully with the users table.")

create_database()
