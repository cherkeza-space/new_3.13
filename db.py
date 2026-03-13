import sqlite3

def create_db():
    conn = sqlite3.connect('mobile_app_data.db')  
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS app_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    difficulty TEXT NOT NULL DEFAULT 0)''')

    conn.commit()
    conn.close()

create_db()