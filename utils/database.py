import sqlite3
import os


DB_PATH = "database/prediction_history.db"


def get_connection():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_prediction_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            image_type TEXT,
            disease TEXT,
            confidence REAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(username, image_type, disease, confidence):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history
        (username, image_type, disease, confidence)
        VALUES (?, ?, ?, ?)
    """, (
        username,
        image_type,
        disease,
        confidence
    ))

    conn.commit()
    conn.close()


def get_history(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM history
        WHERE username = ?
        ORDER BY date DESC
    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data
