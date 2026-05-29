from flask import Blueprint, render_template, session, redirect, url_for, request
from sqlalchemy import select
from models.user import db
from models.chat import MessageInChat
from forms.chat import ChatForm
from forms.terminal import TerminalForm


desktop_blueprint = Blueprint("desktop_pages", __name__,
                      template_folder="templates_desktop")


@desktop_blueprint.route("/main")
def main_desktop():
    if "username" in session:
        return render_template("main.html")
    return redirect(url_for("auth_pages.auth_page"))


@desktop_blueprint.route("/win", methods=["GET", "POST"])
def profile_desktop():
    if "username" in session:
        user = session["username"]
        return render_template("win.html", user=user)
    return redirect(url_for("auth_pages.auth_page"))


@desktop_blueprint.route("/chat", methods=["GET", "POST"])
def chat_desktop():
    form = ChatForm()
    if "username" in session:
        user = session["username"]
        messages = db.session.execute(select(MessageInChat)).scalars().all()
        if form.validate_on_submit():
            message = request.form["message"]
            request_message = MessageInChat(
                username=user,
                message = message
            )
            db.session.add(request_message)
            db.session.commit()
        return render_template("chat.html", messages=messages, form=form)
    return redirect(url_for("auth_pages.auth_page"))


@desktop_blueprint.route("/terminal", methods=["GET", "POST"])
def terminal_desktop():
    form = TerminalForm()
    if "username" in session:
        messages = db.session.execute(select(MessageInChat)).scalars().all()
        if form.validate_on_submit():
            message = "Разработчику лень изучать фронтенд"
            return render_template("terminal.html", messages=messages, form=form)
        return render_template("terminal.html", messages=messages, form=form)
    return redirect(url_for("auth_pages.auth_page"))