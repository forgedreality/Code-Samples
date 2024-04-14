import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)
app.secret_key = 'anysecretkey'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# For validating days entered in insert request
totalDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    current_db = db.execute("SELECT * FROM birthdays")

    # Find first available ID
    next_id = 0
    last_id = 0
    for i in range(len(current_db)):
        if i == len(current_db) - 1:
            next_id = str(int(current_db[i]['id']) + 1)
        if abs(last_id - int(current_db[i]['id'])) > 1:
            next_id = str(max(last_id, int(current_db[i]['id'])) - 1)
            break
        last_id = current_db[i]['id']

    # Ensure session exists
    if "birthdays" not in session:
        session["birthdays"] = []

    if request.method == "POST":
        # Get request arguments
        a = request.args

        if a['q'] == 'delete' and int(a['id']) >= 0:
            db.execute("DELETE FROM birthdays WHERE id = ?", a['id'])
            current_db = db.execute("SELECT * FROM birthdays")

        # elif a['q'] == 'update' and int(a['id']) >= 0:
        #     db.execute("DELETE FROM birthdays WHERE id = ?", a['id'])
        #     current_db = db.execute("SELECT * FROM birthdays")

        # else:
        elif a['q'] == 'add':
            # session["birthdays"] = request.form.get("birthdays")
            session["birthdays"] = current_db

            # Add the user's entry into the database
            id = next_id
            name = request.form.get("name")
            month = request.form.get("month")
            day = request.form.get("day")

            if int(month) > 0 and int(month) <= 12 and int(day) > 0 and int(day) <= totalDays[int(month) - 1]:
                db.execute("INSERT INTO birthdays ('id', 'name', 'month', 'day') VALUES (?, ?, ?, ?)", id, name, month, day)

            # if id:
            #     session["birthdays"].append({'id':id, 'name':name, 'month':month, 'day':day})

        return redirect("/")

    else:
        # Display the entries in the database on index.html
        return render_template("index.html", birthdays=current_db)


# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         return render_template("greet.html", name=request.form.get("name", "world"))
#     return render_template("index.html")
