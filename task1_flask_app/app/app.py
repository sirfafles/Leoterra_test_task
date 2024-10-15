import os
import sqlite3

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   url_for)

app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "users.db"


def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)"""
        )
        conn.commit()
        conn.close()


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        ).fetchone()
        conn.close()

        if user:
            return render_template("success.html", message="Вы авторизовались!")
        else:
            flash("Неправильный логин или пароль")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()

        if user:
            flash("Пользователь уже существует!")
            conn.close()
            return redirect(url_for("register"))

        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
        )
        conn.commit()
        conn.close()
        flash("Вы успешно зарегистрировались!")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/items", methods=["GET"])
def get_items():
    items = [
        {
            "id": 1,
            "name": "Item 1",
            "description": "Description for item 1",
            "price": 100,
        },
        {
            "id": 2,
            "name": "Item 2",
            "description": "Description for item 2",
            "price": 200,
        },
        {
            "id": 3,
            "name": "Item 3",
            "description": "Description for item 3",
            "price": 300,
        },
        {
            "id": 4,
            "name": "Item 4",
            "description": "Description for item 4",
            "price": 400,
        },
    ]
    return jsonify(items)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
