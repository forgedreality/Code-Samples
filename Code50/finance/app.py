import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


# CREATE TABLE purchases (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, purchase_date TEXT NOT NULL, user_id INTEGER NOT NULL, symbol TEXT NOT NULL, purchase_price NUMERIC NOT NULL, quantity NUMERIC NOT NULL, total GENERATED ALWAYS AS (purchase_price * quantity) STORED);
# CREATE TABLE owned_stocks_itinerary (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id NUMERIC NOT NULL, symbol TEXT NOT NULL, quantity NUMERIC CHECK (quantity >= 0));
# CREATE TABLE symbols (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, symbol TEXT NOT NULL UNIQUE, name TEXT);

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # summary = db.execute("SELECT symbol, SUM(quantity) AS quantity FROM purchases WHERE user_id = ? AND quantity > 0 GROUP BY symbol", session["user_id"])
    # CREATE TABLE owned_stocks_itinerary (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id NUMERIC NOT NULL, symbol TEXT NOT NULL UNIQUE, quantity NUMERIC CHECK (quantity >= 0));
    summary = db.execute(
        "SELECT symbol, quantity FROM owned_stocks_itinerary WHERE user_id = ? ORDER BY symbol", session["user_id"]
    )

    for i, s in enumerate(summary):
        x = lookup(s['symbol'])
        name = x['name']

        price = x['price']
        sum = price * s['quantity']

        summary[i].update({"total": sum, "name": name})

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
    return render_template("index.html", title="PORTFOLIO OVERVIEW", summary=summary, cash=cash)


@app.route("/profile")
@login_required
def profile():
    """Show profile"""
    # TODO: Add ability to set profile pic, add cash, other data?
    user = db.execute("SELECT username, cash FROM users WHERE id = ?", session["user_id"])
    cash = user[0]['cash']
    name = user[0]['username']

    return render_template("profile.html", title="PROFILE", username=name, cash=cash)


@app.route("/profile_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change Password"""
    if request.method == "POST":
        # check_hash = generate_password_hash(request.form.get("password"))

        old = request.form.get("old_password")
        currHash = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]['hash']

        new = request.form.get("new_password")
        confirm = request.form.get("confirm_password")

        if not check_password_hash(currHash, old):
            return apology("you mistyped your existing password", 403, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/profile_password")

        if new != confirm:
            return apology("passwords do not match", 403, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/profile_password")

        hash = generate_password_hash(request.form.get("new_password"))
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, session["user_id"])

        return render_template("profile_password.html", title="PASSWORD CHANGED", changed=True)

    else:
        return render_template("profile_password.html", title="CHANGE PASSWORD", changed=None)


@app.route("/profile_username", methods=["GET", "POST"])
@login_required
def change_username():
    """Change Username"""
    if request.method == "POST":
        new = request.form.get("new_username").lower()
        confirm = request.form.get("confirm_username").lower()

        if new != confirm:
            return apology("usernames do not match", 403, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/profile_username")

        old = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]['username'].lower()

        if new == old:
            return apology("you tried to change to the same username", 403, back="/profile_username")

        db.execute("UPDATE users SET username = ? WHERE id = ?", new, session["user_id"])

        return render_template("profile_username.html", title=f"USERNAME {old} CHANGED TO {new}", changed=True)

    else:
        return render_template("profile_username.html", title="CHANGE USERNAME")


@app.route("/profile_transfer", methods=["GET", "POST"])
@login_required
def transfer_cash():
    """Transfer Cash"""
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
    if request.method == "POST":
        transfer_amt = abs(float(request.form.get("addcash")))

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", transfer_amt, session["user_id"])

        return render_template("profile_transfer.html", title=f"{usd(transfer_amt)} CASH TRANSFERRED", changed=True)

    else:
        return render_template("profile_transfer.html", title="TRANSFER CASH", cash=cash)


@app.route("/profile_reset", methods=["GET", "POST"])
@login_required
def profile_reset():
    """Reset Profile"""
    if request.method == "POST":
        password = request.form.get("password")
        passHash = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]['hash']

        if not check_password_hash(passHash, password):
            return apology("you mistyped your existing password", 403, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/profile_reset")

        if request.form.get("confirm") != "confirm":
            return apology("you didn't confirm", 403, back="/profile_reset")

        db.execute("DELETE FROM owned_stocks_itinerary WHERE user_id = ?", session["user_id"])
        db.execute("DELETE FROM purchases WHERE user_id = ?", session["user_id"])
        db.execute("DELETE FROM symbols")
        db.execute("UPDATE users SET cash = 10000 WHERE id = ?", session["user_id"])

        return render_template("profile_reset.html", title=f"PROFILE RESET", changed=True)

    else:
        return render_template("profile_reset.html", title="RESET PROFILE")


def get_symbol(sym):
    response = db.execute("SELECT name FROM symbols WHERE symbol = ?", sym)
    if response:
        return response[0]['name']
    return None


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        sym = request.form.get("symbol").upper()
        sha = request.form.get("shares")

        # Ensure stock symbol was submitted
        if not sym:
            return apology("must provide symbol", 400, back="/buy")

        # Ensure number of shares was submitted
        if not sha:
            return apology("must provide quantity", 400, back="/buy")

        try:
            sha = int(sha)
        except:
            return apology("shares must be an integer", 400, back="/buy")

        if sha < 1:
            return apology(f"you can't buy {sha} shares", 400, back="/buy")

        q_response = lookup(sym)

        if not q_response:
            return apology("symbol returned no result", 400, back="/buy")

        # Do we have enough money?
        c = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
        p = q_response['price']

        if c < p * sha:
            return apology("you don't have enough money", 400, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/buy")
        n = q_response['name']

        if request.form.get("fromOverview") == "on":
            return render_template("buy.html", title="BUY", symbol=sym, shares=sha, price=p, default=True)

        # Update symbols table so we can look up the name later when combining with overview pages
        if not get_symbol(sym):
            db.execute("INSERT INTO symbols (symbol, name, last_price) VALUES (?, ?, ?)", sym, n, p)

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", (p * sha), session["user_id"])
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']

        db.execute("INSERT INTO purchases ('purchase_date', 'user_id', 'symbol', 'purchase_price', 'quantity') VALUES (?, ?, ?, ?, ?)",
                   datetime.now(), session["user_id"], sym, p, sha)

        # Check if the stock is already owned by this user and add it if not, or update the quantity if it is
        test = db.execute("INSERT OR IGNORE INTO owned_stocks_itinerary (user_id, symbol, quantity) VALUES (?, ?, ?)",
                          session["user_id"], sym, sha)
        if test == None:
            db.execute("UPDATE owned_stocks_itinerary SET quantity = quantity + ? WHERE user_id = ? AND symbol = ?",
                       sha, session["user_id"], sym)

        owned = db.execute("SELECT quantity FROM owned_stocks_itinerary WHERE user_id = ? AND symbol = ?",
                           session["user_id"], sym)[0]['quantity']
        return render_template("buy.html", title="BUY", symbol=sym, shares=sha, price=p, cash=cash, owned=owned)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html", title="BUY")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    portfolio = db.execute("SELECT * FROM purchases WHERE user_id = ?", session["user_id"])

    # stonks can only go up. :)
    # Get stock names and symbols owned by current user; group by symbol to prevent excessive lookups
    # stonks = db.execute("SELECT symbol FROM purchases WHERE user_id = ? GROUP BY symbol", session["user_id"])
    stonks = db.execute("SELECT p.symbol, s.name FROM purchases p INNER JOIN symbols s ON s.symbol = p.symbol WHERE user_id = ? GROUP BY p.symbol",
                        session["user_id"])

    # Gather current prices from owned stocks
    for p in stonks:
        sym = p['symbol']
        # get current price of stock symbol
        curr_price = lookup(sym)['price']
        db.execute("UPDATE symbols SET last_price = ? WHERE symbol = ?", curr_price, sym)

    # Get the symbol columns stocks owned by current user to pass into history template
    symbols = db.execute("SELECT s.symbol, name, last_price FROM symbols s INNER JOIN purchases p ON s.symbol = p.symbol WHERE user_id = ? GROUP BY s.symbol",
                         session["user_id"])

    for p in portfolio:
        for s in symbols:
            if p['symbol'] == s['symbol'] and 'last_price' not in p:
                p.update({'last_price': s['last_price'], 'name': s['name']})

    # Don't need this anymore
    del symbols
    del stonks

    return render_template("history.html", title=("NO " if not portfolio else "") + "PURCHASE HISTORY", purchases=portfolio)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403, back="/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403, back="/login")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username").lower())

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403, back="/login")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", title="LOG IN")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure stock symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400, back="/quote")

        q_response = lookup(request.form.get("symbol"))

        if not q_response:
            return apology("symbol returned no result", 400, back="/quote")

        if not q_response['name']:
            return apology(f"symbol seems invalid. perhaps {q_response['symbol']} has been delisted?", 400, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/quote")

        return render_template("quote.html", title="GET QUOTE", quote=q_response)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html", title="GET QUOTE")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400, back="/register")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400, back="/register")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username").lower())

        # Ensure username exists and password is correct
        if len(rows) == 1:
            return apology("username already taken", 400, back="/register")

        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        if password != confirm:
            return apology("passwords do not match", 400, "https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/profile_password")

        # Insert new user into db
        db.execute("INSERT INTO users ('username', 'hash', 'cash') VALUES (?, ?, ?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")), 10000)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username").lower())

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html", title="REGISTER")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    summary = db.execute("SELECT symbol, SUM(quantity) AS quantity FROM owned_stocks_itinerary WHERE user_id = ? GROUP BY symbol",
                         session["user_id"])

    # Update our local summary with current stock prices
    for i, s in enumerate(summary):
        x = lookup(s['symbol'])
        price = x['price']
        summary[i].update({"price": price})

    if request.method == "POST":
        sym = request.form.get("symbol")
        sha = request.form.get("shares")

        obj = None

        # Get our current stock statistics for use in subsequent SQL queries
        for s in summary:
            if s['symbol'] == sym:
                obj = s
                break

        # Set var representing current price of stock
        price = obj['price']

        if request.form.get("fromOverview") == "on":
            return render_template("sell.html", title="SELL", summary=summary, symbol=sym, shares=sha, default=True)

        try:
            sha = int(sha)
        except:
            return apology("shares must be an integer", 400, back="/sell")

        if sha < 1:
            return apology(f"you can't sell {sha} shares", 400, back="/sell")

        if not obj:
            return apology(f"you don't own any {sym} shares", 400, img="https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/sell")

        if sha > obj['quantity']:
            return apology(f"you don't own {sha} {sym} shares", 400, img="https://i.kym-cdn.com/entries/icons/original/000/037/224/DdJoHa8XUAIClgI.jpeg", back="/sell")

        # [{'symbol': 'amd', 'quantity': 43, 'price': 77.63}, {'symbol': 'goog', 'quantity': 4, 'price': 101.45}, {'symbol': 'nvda', 'quantity': 38, 'price': 169.23}]

        # +----+---------------------+---------+--------+----------------+----------+---------+
        # | id |    purchase_date    | user_id | symbol | purchase_price | quantity |  total  |
        # +----+---------------------+---------+--------+----------------+----------+---------+
        # | 10 | 2022-11-30 07:05:19 | 1       | nvda   | 156.39         | 15       | 2345.85 |
        # | 11 | 2022-11-30 07:51:21 | 1       | nvda   | 156.39         | 23       | 3596.97 |
        # | 12 | 2022-11-30 08:07:18 | 1       | amd    | 73.39          | 43       | 3155.77 |
        # | 13 | 2022-11-30 08:22:29 | 1       | goog   | 95.44          | 1        | 95.44   |
        # | 14 | 2022-11-30 08:22:40 | 1       | goog   | 95.44          | 3        | 286.32  |
        # +----+---------------------+---------+--------+----------------+----------+---------+
        db.execute("INSERT INTO purchases ('purchase_date', 'user_id', 'symbol', 'purchase_price', 'quantity') VALUES (?, ?, ?, ?, ?)",
                   datetime.now(), session["user_id"], sym, obj['price'], -abs(sha))

        db.execute("UPDATE owned_stocks_itinerary SET quantity = quantity - ? WHERE user_id = ? AND symbol = ?",
                   sha, session["user_id"], sym)
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", (price * sha), session["user_id"])
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']

        if db.execute("SELECT quantity FROM owned_stocks_itinerary WHERE user_id = ? AND symbol = ?", session["user_id"], sym)[0]['quantity'] == 0:
            db.execute("DELETE FROM owned_stocks_itinerary WHERE user_id = ? AND symbol = ?", session["user_id"], sym)

        owned = db.execute("SELECT quantity FROM owned_stocks_itinerary WHERE user_id = ? AND symbol = ?",
                           session["user_id"], sym)[0]['quantity']
        return render_template("sell.html", title="SELL", summary=summary, symbol=sym, shares=sha, price=price, cash=cash, owned=owned)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html", title="NO SHARES OWNED" if not summary else "SELL", summary=summary)
