from app import app, db
from flask import render_template, request, session, redirect
from models.models import Plant, User


@app.route("/")
def main():
    plants = Plant.query.order_by(Plant.title.asc()).all()
    # plants = Plant.query.filter(Plant.location == "st. Mariupol ") фильтр по адресу
    print(plants)
    user = None
    if session.get("user", False):
        user = User.query.get(session.get("user"))
    return render_template("index.html", plants=plants, user=user)

@app.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        data = request.form
        user = User(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name")
        )
        db.session.add(user)
        db.session.commit()
        session["user"] =user.id
        return redirect("/")
    else:
        return render_template("sign-up.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/sign-in", methods=["POST", "GET"])
def sign_in():
    if request.method == "POST":
        data = request.form
        user = User(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name")
        )
        db.session.add(user)
        db.session.commit()
        session["user"] =user.id
        return redirect("/")
    else:
        return render_template("sign-in.html")