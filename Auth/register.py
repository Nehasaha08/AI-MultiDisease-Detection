import sqlite3
from Auth.auth_utils import hash_password


def register_user(username, password):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    try:
        hashed_password = hash_password(password)

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:
        conn.close()
        return False
