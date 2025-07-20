from detector import detect_sqli
from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "logs.txt"

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # replace with your MySQL password
        database="sqli_demo"
    )

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")
    conn.commit()
    conn.close()

def log_attempt(query, response):
    flag = "[SQLi DETECTED]" if "Detected" in response else "[OK]"
    log = f"{datetime.now()} {flag} - Query: {query} - Response: {response}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vulnerable-login", methods=["GET", "POST"])
def vulnerable_login():
    message = ""
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]

        conn = get_db_connection()
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{uname}' AND password='{pwd}'"
        try:
            c.execute(query)
            result = c.fetchone()
            if result:
                message = "Login Successful (Vulnerable)!"
            else:
                message = "Login Failed!"
        except Exception as e:
            message = "Error in query execution."
        conn.close()
        log_attempt(query, message)
    return render_template("login.html", message=message)

@app.route("/secure-login", methods=["GET", "POST"])
def secure_login():
    message = ""
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]

         # Detection step
        if detect_sqli(uname) or detect_sqli(pwd):
            message = "⚠️ SQL Injection Detected! Request blocked."
            log_attempt(f"Blocked Input: username={uname}, password={pwd}", message)
            return render_template("login.html", message=message)

        conn = get_db_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM users WHERE username=%s AND password=%s", (uname, pwd))
            result = c.fetchone()
            if result:
                message = "Login Successful (Secure)!"
            else:
                message = "Login Failed!"
        except Exception as e:
            message = "Error in query execution."
        conn.close()
        log_attempt("SECURE_QUERY", message)
    return render_template("secure_login.html", message=message)

@app.route("/logs")
def logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            log_data = f.readlines()
    else:
        log_data = ["No logs found."]
    return render_template("logs.html", logs=log_data)

if __name__ == "__main__":
    
    app.run(debug=True)
