from flask import Blueprint, render_template, session, redirect, url_for, request


desktop_blueprint = Blueprint("desktop_pages", __name__,
                      template_folder="templates_desktop")


@desktop_blueprint.route("/main")
def main_desktop():
    return render_template("main.html")


@desktop_blueprint.route("/win", methods=["GET", "POST"])
def profile_desktop():
    return render_template("win.html")