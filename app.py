import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def budget_app():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        password = request.form.get("password")
        check_password = request.form.get("confirm-password")
        email = request.form.get("email")
        check_email = request.form.get("confirm-email")

        if password != check_password:
            flash("Please make sure the passwords match")
            return redirect(url_for("signup"))

        if email != check_email:
            flash("Please make sure the emails match")
            return redirect(url_for("signup"))

        new_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        x = 0

        categories = {
            "username": request.form.get("username").lower(),
            "income": float(x),
            "rent": float(x),
            "utilities": float(x),
            "car": float(x),
            "debt": float(x),
            "groceries": float(x),
            "travel": float(x),
            "subscriptions": float(x),
            "holiday": float(x),
            "misc": float(x),
            "total": float(x)
        }
        mongo.db.categories.insert_one(categories)

        account_balance = request.form.get("account-balance")
        
        balance = {
            "username": request.form.get("username").lower(),
            "account_balance": account_balance
        }
        mongo.db.balance.insert_one(balance)

        session["user"] = request.form.get("username").lower()
        flash("Register complete")
        return redirect(url_for("budget_app"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("budget_app"))
            else:
                flash("Inccorect username and/or password")
                return redirect(url_for("login"))
        else:
            flash("Inccorect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash ("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_record", methods=["GET", "POST"])
def add_record():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    categories = mongo.db.categories.find_one(
        {"username": session["user"]})
    
    if request.method == "POST":
        record_id = 1
        date = request.form.get("date")
        card = request.form.get("card")
        name = request.form.get("name")
        category = request.form.get("category")
        amount = request.form.get("amount")
        notes = request.form.get("notes")
        balance = mongo.db.balance.find_one(
            {"username": session["user"]})["account_balance"]

        if category == "income":
            new_balance = float(balance) + float(amount)
        else:
            new_balance = float(balance) - float(amount)

        record = {
            "username": username,
            "record_id": record_id,
            "date": date,
            "card": card,
            "name": name,
            "category": category,
            "amount": float(amount),
            "notes": notes,
            "balance": float(new_balance),
        }
        mongo.db.records.insert_one(record)

        update_balance = {
            "account_balance": new_balance
        }
        mongo.db.balance.update_one({"username": username}, {"$set": update_balance})

        # income = 0
        # category_id = ""
        # print(category + " = Selected category")
        # # Temporary
        
        # for i in mongo.db.categories.find_one({"username": session["user"]}):
        #     print(i)

        # # Temporary
        #     if category == "income":
        #         income = float(amount) + categories["income"]
        #         update_categories = {
        #             "income": income
        #         }
        #     else:
        #         if i == category:
        #             category_old = categories[i]
        #             category_sum = float(amount) + category_old
        #             total_sum = float(category_sum) + categories["total"]
        #             print(i + " TEST")
        #             print("---- Amount ----")
        #             print(amount)
        #             print("---- Old Balance ----")
        #             print(category_old)
        #             print("---- New Balance ----")
        #             print(category_sum)
                    
        #             update_categories = {
        #                 "rent": category_sum,
        #                 "utilities": 0,
        #                 "car": 0,
        #                 "debt": 0,
        #                 "groceries": 0,
        #                 "travel": 0,
        #                 "subscriptions": 0,
        #                 "holiday": 0,
        #                 "misc": 0,
        #                 "total": total_sum
        #             }
        #             break
        #         # Temporary

        # mongo.db.categories.update_one({"username": username}, {"$set": update_categories})
        # flash("Record successfully added")
        # print(categories)

    return render_template("add_record.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)