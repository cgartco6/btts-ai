import sqlite3

conn = sqlite3.connect("btts_ai.db", check_same_thread=False)

def init_db():
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        match_id TEXT PRIMARY KEY,
        league TEXT,
        home TEXT,
        away TEXT,
        date TEXT,
        home_goals INT,
        away_goals INT,
        btts INT
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS odds (
        match_id TEXT,
        bookmaker TEXT,
        btts_yes REAL,
        btts_no REAL,
        ts DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
