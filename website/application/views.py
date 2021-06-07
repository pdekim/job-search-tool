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

@view.route('/index_get_data')
def data():
    data = {
        "data": [
        {
            "id": "1",
            "date": "05/02/2021",
            "company": "Amazon",
            "position": "Sofware Engineer I",
            "experience": "Entry",
            "status": "Applied"
        },
        {
            "id": "2",
            "date": "04/11/2021",
            "company": "Facebook",
            "position": "Sofware Engineer I",
            "experience": "Associate",
            "status": "Applied"
        },
        {
            "id": "3",
            "date": "07/12/2021",
            "company": "Facebook",
            "position": "Sofware Engineer I",
            "experience": "Associate",
            "status": "Applied"
        },
        {
            "id": "4",
            "date": "07/11/2020",
            "company": "Facebook",
            "position": "Sofware Engineer I",
            "experience": "Associate",
            "status": "Applied"
        },
        ]
    }

    return jsonify(data)


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
