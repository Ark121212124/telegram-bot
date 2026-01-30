import sqlite3

# подключение к базе
conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# ===== ТАБЛИЦА НОВОСТЕЙ =====
cursor.execute("""
CREATE TABLE IF NOT EXISTS news(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    text TEXT,
    photo TEXT,
    link TEXT
)
""")

# ===== ТАБЛИЦА ПОДПИСЧИКОВ =====
cursor.execute("""
CREATE TABLE IF NOT EXISTS subs(
    user_id INTEGER UNIQUE
)
""")

# ===== ТАБЛИЦА ОБРАЩЕНИЙ =====
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    message TEXT
)
""")

# сохраняем изменения
conn.commit()
