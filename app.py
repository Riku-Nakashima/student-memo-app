from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("memo.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()

    # 生徒追加
    if request.method == "POST":
        name = request.form["name"]
        grade = request.form["grade"]
        conn.execute(
            "INSERT INTO students (name, grade) VALUES (?, ?)",
            (name, grade)
        )
        conn.commit()
        return redirect("/")

    # 検索
    keyword = request.args.get("q")

    if keyword:
        students = conn.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            (f"%{keyword}%",)
        ).fetchall()
    else:
        students = conn.execute(
            "SELECT * FROM students"
        ).fetchall()

    conn.close()
    return render_template("index.html", students=students)

@app.route("/student/<int:student_id>", methods=["GET", "POST"])
def student_detail(student_id):
    conn = get_db_connection()

    if request.method == "POST":
        subject = request.form["subject"]
        content = request.form["content"]
        today = date.today().isoformat()
        conn.execute(
            "INSERT INTO notes (student_id, date, subject , content) VALUES (?, ?, ? ,?)",
            (student_id, today, subject , content)
        )
        conn.commit()
        return redirect(f"/student/{student_id}")

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    notes = conn.execute(
        "SELECT * FROM notes WHERE student_id = ? ORDER BY date DESC",
        (student_id,)
    ).fetchall()

    conn.close()
    return render_template(
        "student.html",
        student=student,
        notes=notes
    )
@app.route("/note/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    conn = get_db_connection()
    student_id = conn.execute(
        "SELECT student_id FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()["student_id"]

    conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

    return redirect(f"/student/{student_id}")
@app.route("/student/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM notes WHERE student_id = ?", (student_id,))
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
