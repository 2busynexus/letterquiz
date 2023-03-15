from flask import Flask, render_template, redirect, url_for, request, session
from forms import loginForm, signUpForm, gameForm, changeEmailForm, changePasswordForm
import random


from mysqlconn import *
from checks import *


app = Flask(__name__)

#form configuration
app.config['SECRET_KEY'] = "mysecretkey135"
 

@app.route("/")
def index():
    if "user" in session:
        session.pop("user")
    if "profile" in session:
        session.pop("profile")
    if "points" in session:
        session.pop("points")
    return render_template("index.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    login = loginForm()
    if login.validate_on_submit():

        if "user" in session:
            session.pop("user")

        if checkLogin(login.username.data, login.password.data):
            session["user"] = login.username.data
            return redirect(url_for("profile"))
        else:
            return render_template("login.html",form=login, error = "Login failed!")
    return render_template("login.html", form = login)

@app.route("/signup", methods = ['GET', 'POST'])
def signUp():
    signUp = signUpForm()
    if signUp.validate_on_submit():

        if "user" in session:
            session.pop("user")

        if checkSignUp(signUp.username.data, signUp.email.data, signUp.password.data):
            session["user"] = signUp.username.data
            return redirect(url_for("profile"))
        else:
            return render_template("signup.html", form=signUp, error="Username or email already exists!")
    return render_template("signup.html", form = signUp)

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    
    changeEmail = changeEmailForm()
    changePassword = changePasswordForm()
    #print(session)
    if "user" in session:
        session["profile"] = getProfile(session["user"])
    else:
        return redirect(url_for("error"))

    #change email form
    if request.method=="POST" and changeEmail.validate_on_submit():
        if changeEmail.email.data:
            if updateUser("email", changeEmail.email.data, session["user"]):
                global emailError
                emailError="Email changed"
            else:
                emailError="Email already exists"
            return render_template("profile.html", changeEmail=changeEmail, changePassword=changePassword, emailError=emailError)

    #change password form
    if request.method=="POST" and changePassword.validate_on_submit():
        print(type(changePassword.password.data))
        if changePassword.password.data:
            updateUser("password", changePassword.password.data, session["user"])
            passError="Password changed"
            return render_template("profile.html", changeEmail=changeEmail, changePassword=changePassword, passError=passError)
    elif request.method=="POST" and not changePassword.validate_on_submit():
            passError="Password not matching"
            return render_template("profile.html", changeEmail=changeEmail, changePassword=changePassword, passError=passError)

    return render_template("profile.html", changeEmail=changeEmail, changePassword=changePassword)

@app.route("/delete")
def delete():
    deleteUser(session["user"])
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/game", methods = ['GET', 'POST'])
def game():
    #print(session)
    if "user" not in session:
        return redirect(url_for("error"))
    session["profile"] = getProfile(session["user"])
    if request.method == "GET":
        global generatedLetter
        generatedLetter = random.choice(letters)
        global data
        data = {
            "countries": countriesRows(generatedLetter),
            "cities": citiesRows(generatedLetter),
            "waters": watersRows(generatedLetter),
            "mountains": mountainsRows(generatedLetter),
            "crops": cropsRows(generatedLetter),
            "animals": animalsRows(generatedLetter)
        }
        #print(generatedLetter)
        #print(data)
    form = gameForm()
    if request.method == "POST":
        answers = {
            "country": form.countryPick.data,
            "city": form.cityPick.data,
            "water": form.waterPick.data,
            "mountain": form.mountainPick.data,
            "crop": form.cropPick.data,
            "animal": form.animalPick.data
        }
        #print(answers)
        checks = {
            "country": allRows(answers["country"], data["countries"]),
            "city": allRows(answers["city"], data["cities"]),
            "water": allRows(answers["water"], data["waters"]),
            "mountains": allRows(answers["mountain"], data["mountains"]),
            "crop": allRows(answers["crop"], data["crops"]),
            "animal": allRows(answers["animal"], data["animals"])
        }
        #print(checks)
        points = score(checks)
        #print(points)
        session["points"] = points
        addHighscore(points, session["user"])
        return redirect(url_for("check", points=points))
    return render_template("game.html",form=form, letter=generatedLetter)


@app.route("/check")
def check():
    
    points = session["points"]

    return render_template("check.html", points=points)

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
