import sqlite3

# データベースに接続（なければ自動で作られる）
conn = sqlite3.connect("memo.db")
cur = conn.cursor()

# students テーブル
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade TEXT
);
""")

# notes テーブル
cur.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    subject TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
""")

conn.commit()
conn.close()

print("データベースを初期化しました")
