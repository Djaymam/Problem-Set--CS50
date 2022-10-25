import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

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
    #geting the user ID
    userID = session["user_id"]
    
    #geting infor in database
    transactions_db = db.execute("SELECT company, SUM(shares) AS shares, price FROM userstransaction WHERE userId=? GROUP BY company",userID)
    
    #company_symbol = transactions_db[0]["company"] #paremeter for lookup() function
    #stock = lookup(company_symbol.upper)
    
    #total_value = stock["price"] * transactions_db[1]["shares"]
    
    user_money_db = db.execute("SELECT cash FROM users WHERE id=?", userID) #the data from the database comes in JSON 
    
    user_money = user_money_db[0]["cash"] #geting cash value in the JSON
    
    return render_template("index.html", database = transactions_db , user_money = user_money) #obs: databese is a list Carefull <3
    
    
    
    

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
        
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        
        if not symbol:
            return apology("Insert a Symbol!!")
        
        #validate if the symbol exist in API Database using the lookup() Funtion
        stock = lookup(symbol.upper())
        
        if stock == None:
            return apology("That Symbol Does Not Exist, Like Your GF!")
            
        if shares <= 0:
            return apology("You can't Buy Zero or Negative Shares!! Be Smart!!")
        
        #calculate the shares value that the user is buying
        
        transaction_value = shares * stock["price"]
        
        userID = session["user_id"]  #geting the user id in the session
        
        user_money_db = db.execute("SELECT cash FROM users WHERE id=?", userID) #the data from the database comes in JSON 
        
        user_money = user_money_db[0]["cash"] #geting cash value in the JSON 
        
        #validate if user have money to buy shares
        
        if transaction_value > user_money:
            return apology("Get More Money to Buy This Much!! Go Work!")
            
        #update the user money afther buying the shares
        user_money_after_trans= user_money - transaction_value
        
        db.execute("UPDATE users SET cash=? WHERE id=?;",user_money_after_trans,userID)
        
        #adding the buy information in database finance
        
        date = datetime.datetime.now()
        
        db.execute("INSERT INTO userstransaction (userID, company, shares , price, total, date) VALUES(?, ?, ?, ?, ?, ?)", userID, stock["symbol"], shares, stock["price"], transaction_value, date)
        
        flash("Success!!")
        return redirect("/")
        
        
        

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userID = session["user_id"]
    transaction_db = db.execute("SELECT  * FROM userstransaction WHERE userId=?",userID)
    return render_template("history.html", transaction = transaction_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

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
    
    if request.method == "GET":
        return render_template("quote.html")
    
    else:
        #validation if the symbol that user inputed is valid!
        symbol = request.form.get("symbol")
        
        if not symbol:
            return apology("Insert a Symbol!!")
        
        #check if the symbol exist in Database using the lookup() Funtion
        stock = lookup(symbol.upper())
        
        if stock == None:
            return apology("That Symbol Does Not Exist, Like Your GF!")
        
        return render_template("quoted.html", name = stock["name"], price = stock["price"], symbol = stock["symbol"])

#Personal Touch <3 The user can buy the shares in the qouted page
@app.route("/quoted", methods=["GET", "POST"])
@login_required
def quotedbuy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_templates("quote.html")
        
    else:
        return redirect("/buy.html")
        
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method=="GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        #validate the Users Information when Create new Account
        if not username:
            return apology("Must Enter UserName SmartAss!!")
            
        if not password:
            return apology("You need a password!! OMG!")
            
        if not confirmation:
            return apology("Confirm You Email Man or Woman or Cat!!")
            
        if password != confirmation:
            return apology("You must put the same Password!")
            
        #Secury the user password using werkzeug.security  
        hash = generate_password_hash(password)
        
        #Inserting the new user data in Database
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        except:
            return apology("Username Alredy Taken! Like you Ex-GF!!")
        
        #saving user section
        
        session["user_id"] = new_user
        
        #redirect user to the login page
        
        return redirect("/")
        

@app.route("/sell", methods=["GET", "POST"])
@login_required 
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        #get the companys in the user database
        symbols_user = db.execute ("SELECT company FROM userstransaction WHERE userId = ? GROUP BY company HAVING SUM(shares) > 0", user_id)
        return render_template("sell.html", symbols = [row["company"] for row in symbols_user])
        
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        
        if not symbol:
            return apology("Insert a Symbol!!")
        
        #validate if the symbol exist in API Database using the lookup() Funtion
        stock = lookup(symbol.upper())
        
        if stock == None:
            return apology("That Symbol Does Not Exist, Like Your GF!")
            
        if shares <= 0:
            return apology("You can't Buy Zero or Negative Shares!! Be Smart!!")
            
        
        #calculate the shares value that the user is Selling
        
        transaction_value = shares * stock["price"]
        
        
        userID = session["user_id"]  #geting the user id in the session
        
        user_money_db = db.execute("SELECT cash FROM users WHERE id=?", userID) #the data from the database comes in JSON 
        
        user_money = user_money_db[0]["cash"] #geting cash value in the JSON 
        
        user_shares_db = db.execute("SELECT SUM(shares) AS shares FROM userstransaction WHERE userId=? AND company = ? GROUP BY company", userID, symbol) 
        user_share = user_shares_db[0]["shares"]
        
        if shares > user_share:
            return apology("You Dont Have That Much Shares!!")
    
        #update the user money afther buying the shares
        user_money_after_trans= user_money + transaction_value
        
        shares = (-1) * shares  #converting shares in negative

        db.execute("UPDATE users SET cash=? WHERE id=?;",user_money_after_trans,userID)
        
        #adding the buy information in database finance
        
        date = datetime.datetime.now()
        
        db.execute("INSERT INTO userstransaction (userID, company, shares , price, total, date) VALUES(?, ?, ?, ?, ?, ?)", userID, stock["symbol"],shares, stock["price"], transaction_value, date)
        
        flash("Success!!")
        return redirect("/")
        
        
        
