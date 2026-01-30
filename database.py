import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS news(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
text TEXT,
photo TEXT,
link TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subs(
user_id INTEGER UNIQUE
)
""")

conn.commit()
