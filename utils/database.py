```python
import sqlite3
import os

# Database location
DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "prediction_history.db")


def create_prediction_table():
    # Create database folder if it doesn't exist
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
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


def save_prediction(
    username,
    image_type,
    disease,
    confidence
):
    # Make sure folder exists
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
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
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM history WHERE username=?",
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data
```
