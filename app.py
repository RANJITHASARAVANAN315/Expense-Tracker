from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # change if needed
        password="3105",# change if needed
        database="expense_db"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        category = request.form["category"]
        amount = request.form["amount"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO expenses (category, amount, date) VALUES (%s, %s, %s)",
            (category, amount, date)
        )
        db.commit()
        db.close()

        return redirect("/view")
    return render_template("add_expenses.html")

@app.route("/view")
def view_expense():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    db.close()

    return render_template("view_expenses.html", expenses=data)

@app.route("/total")
def total_expense():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()
    return render_template("total_expense.html", total=result[0] or 0)

if __name__ == "__main__":
    app.run(debug=True)

