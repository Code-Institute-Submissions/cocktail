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
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_ingredients")
def get_ingredients():
    ingredients = mongo.db.ingredients.find()
    return render_template("get_ingredients.html", ingredients=ingredients)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    ingredients = list(mongo.db.ingredients.find(
        {"$text":{"$search":query}}))
    return render_template("get_ingredients.html", ingredients=ingredients)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if request.method == "POST":
        ingredient = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "description_cocktail": request.form.get("description_cocktail"),
            "ice": request.form.get("ice"),
            "garnish": request.form.get("garnish"),
            "method": request.form.get("method"),
            "comment": request.form.get("comment"),
            "image_url": request.form.get("image_url"),
            "glass": request.form.get("glass"),
            "created_by": session["user"]
        }
        mongo.db.ingredients.insert_one(ingredient)
        flash("Cocktail has been added.")
        return redirect(url_for("add_cocktail"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_cocktail.html", categories=categories)


@app.route("/edit_cocktails/<ingredient_id>", methods=["GET", "POST"])
def edit_cocktail(ingredient_id):
    if request.method == "POST":
        submit_cocktail = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "description_cocktail": request.form.get("description_cocktail"),
            "ice": request.form.get("ice"),
            "garnish": request.form.get("garnish"),
            "method": request.form.get("method"),
            "comment": request.form.get("comment"),
            "image_url": request.form.get("image_url"),
            "glass": request.form.get("glass"),
            "created_by": session["user"]
        }
        mongo.db.ingredients.update(
            {"_id": ObjectId(ingredient_id)}, submit_cocktail)
        flash("Cocktail has been update.")
        
    ingredient = mongo.db.ingredients.find_one(
        {"_id": ObjectId(ingredient_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_cocktail.html", ingredient=ingredient ,categories=categories)


@app.route("/delete_cocktail/<ingredient_id>")
def delete_cocktail(ingredient_id):
    mongo.db.ingredients.remove({"_id": ObjectId(ingredient_id)})
    flash("Cocktail has been deleted.")
    return redirect(url_for("get_ingredients"))


@app.route("/get_cocktails")
def get_cocktails():
    cocktails = list(mongo.db.ingredients.find().sort("category_name", 1))
    return render_template("cocktails.html", cocktails=cocktails)


@app.route("/search_cocktails", methods=["GET", "POST"])
def search_cocktails():
    query = request.form.get("query")
    cocktails = list(mongo.db.ingredients.find({"$text":{"$search":query}}))
    return render_template("cocktails.html", cocktails=cocktails)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
