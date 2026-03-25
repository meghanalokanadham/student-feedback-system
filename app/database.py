import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'feedback.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_feedback(name, message):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (name, message) VALUES (?, ?)', (name, message))
    conn.commit()
    conn.close()

def get_all_feedback():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT name, message, submitted_at FROM feedback ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    return [{'name': r[0], 'message': r[1], 'submitted_at': r[2]} for r in rows]
