from flask import Blueprint, render_template, session, redirect, url_for, request
from forms.auth import AuthForm, RegistrationForm
from models.user import User, db


auth_blueprint = Blueprint("auth_pages", __name__,
                      template_folder="templates_auth")

@auth_blueprint.route("/registration", methods=["POST", "GET"])
def registration_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"]
        )
        print(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("desktop_pages.main_desktop"))
    return render_template("auth/registration.html", form=form)


@auth_blueprint.route("/authentication", methods=["GET", "POST"])
def auth_page():
    form = AuthForm()
    if form.validate_on_submit():
        print("Удачный вход")
    return render_template("auth/auth.html", form=form)