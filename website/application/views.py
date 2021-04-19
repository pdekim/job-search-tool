from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import DataBase

view = Blueprint("views", __name__)

# Global constants
NAME_KEY = 'name'

# Views
@view.route("/login", methods=["POST", "GET"])
def login():
    """
    displays main login page and handles saving name in session
    :exception POST
    :return: None
    """
    if request.method == "POST":  # if user input a name
        name = request.form["inputName"]
        if name:
            session[NAME_KEY] = name
            flash(f'You were successfully logged in as {name}.')
            return redirect(url_for("views.home"))
        else:
            flash("There was an error. Please try again.")

    return render_template("login.html", **{"session": session})


@view.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return: None
    """
    session.pop(NAME_KEY, None)
    flash("You were logged out.")
    return redirect(url_for("views.login"))


@view.route("/")
@view.route("/home")
def home():
    """
    displays home page if logged in
    :return: None
    """
    if NAME_KEY not in session:
        return redirect(url_for("views.login"))

    return render_template("index.html", **{"session": session})


@view.route("/analysis")
def analysis():
    """
    displays analysis page if logged in
    :return: None
    """
    if NAME_KEY not in session:
        return redirect(url_for("views.login"))

    return render_template("analysis.html", **{"session": session})
