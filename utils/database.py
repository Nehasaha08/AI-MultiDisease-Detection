import sqlite3

def create_prediction_table():

    conn = sqlite3.connect(
        "database/prediction_history.db"
    )

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
        confidence):

    conn = sqlite3.connect(
        "database/prediction_history.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history
    (username,image_type,disease,confidence)
    VALUES(?,?,?,?)
    """,
    (
        username,
        image_type,
        disease,
        confidence
    ))

    conn.commit()
    conn.close()


def get_history(username):

    conn = sqlite3.connect(
        "database/prediction_history.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM history WHERE username=?",
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data