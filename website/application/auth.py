from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import Database

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
    """
    displays main login page and handles saving name in session
    :exception POST
    :return: None
    """
    if request.method == "POST":  # if user attempts to login
        email = request.form["inputName"]
        if username:
            session[NAME_KEY] = username
            flash(f'You were successfully logged in as {username}.')
            return redirect(url_for("views.home"))
        else:
            flash("There was an error. Please try again.")

    return render_template("login.html", **{"session": session})

@auth.route('/signup', methods=['POST'])
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

        # search in database if email already exists
        # if not, create new user entry in database
        return redirect(url_for('auth.login'))

    return render_template("signup.html")

@auth.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return: None
    """
    session.pop(NAME_KEY, None)
    flash("You were logged out.")
    return redirect(url_for("auth.login"))