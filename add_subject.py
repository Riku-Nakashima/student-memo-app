import sqlite3

conn = sqlite3.connect("memo.db")
conn.execute("ALTER TABLE notes ADD COLUMN subject TEXT")
conn.commit()
conn.close()

print("subject カラムを追加しました")
