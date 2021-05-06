from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import Database
import bcrypt 

auth = Blueprint('auth', __name__)

# Global constants
USER_KEY = 'name'

@auth.route("/login", methods=["POST", "GET"])
def login():
    """
    displays main login page and handles saving name in session
    :exception POST
    :return: None
    """
    if request.method == "POST":  # if user attempts to login
        email = request.form["email"]
        password = request.form['password']

        db = Database()
        user_info = db.get_user_info(email)

        if not user_info:
            flash("Your email isn't tied to an account. Please sign up and try again.")
            return redirect(url_for('auth.login'))
        elif check_password(password, user_info[0][2]):
            session[USER_KEY] = user_info[0][0]
            flash(f'You were successfully logged in as {user_info[0][0]}.')
            return redirect(url_for("views.home"))
        else:
            flash("Incorrect Password. Please try again.")

    return render_template("login.html", **{"session": session})


@auth.route('/signup', methods=["POST", "GET"])
def signup():
    """
    displays signup page
    :exception POST
    :return: None
    """
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        encrypted_password = get_hashed_password(password)

        db = Database()

        if db.get_user_info(email):
            flash(f'The email address is already taken. Please choose another one.')
            return redirect(url_for('auth.signup'))
        else:
            db.save_new_user(name, email, encrypted_password)

        return redirect(url_for('auth.login'))

    return render_template("signup.html")


@auth.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return: None
    """
    session.pop(USER_KEY, None)
    flash("You were logged out.")
    return redirect(url_for("auth.login"))



# UTILITIES

# used implementation from: https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
# for hash and salt password
def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    # (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)
