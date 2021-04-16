from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint

view = Blueprint("views", __name__)

@view.route("/")
def main():
    return "Welcome!"


@view.route('/how are you')
def hello():
    return 'I am good, how about you?'