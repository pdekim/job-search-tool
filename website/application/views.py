from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import Database

view = Blueprint("views", __name__)

# Global constants
USER_KEY = 'name'

# Views
@view.route("/")
@view.route("/home")
def home():
    """
    displays home page if logged in
    :return: None
    """
    if USER_KEY not in session:
        flash("Please login to view your home page.")
        return redirect(url_for("auth.login"))

    return render_template("index.html", **{"session": session})


@view.route("/analysis")
def analysis():
    """
    displays analysis page if logged in
    :return: None
    """
    if USER_KEY not in session:
        flash("Please login to view your analysis page.")
        return redirect(url_for("auth.login"))

    return render_template("analysis.html", **{"session": session})
