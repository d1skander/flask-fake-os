from flask import Blueprint, render_template, session, redirect, url_for, request
from forms.auth import AuthForm, RegistrationForm
from models.user import User, db
from sqlalchemy import select, delete


auth_blueprint = Blueprint("auth_pages", __name__,
                      template_folder="templates_auth")

@auth_blueprint.route("/registration", methods=["POST", "GET"])
def registration_page():
    from main import bcrypt
    form = RegistrationForm()
    if form.validate_on_submit():
        no_hash_password = request.form["password"]
        hash_password = bcrypt.generate_password_hash(no_hash_password).decode("utf-8")
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=hash_password
        )
        db.session.add(user)
        db.session.commit()
        session["username"] = request.form["username"]
        return redirect(url_for("desktop_pages.main_desktop"))
    return render_template("auth/registration.html", form=form)


@auth_blueprint.route("/authentication", methods=["GET", "POST"])
def auth_page():
    from main import bcrypt
    form = AuthForm()
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        user = db.session.execute(select(User).filter_by(username=username)).scalar_one()
        hash_password = bcrypt.check_password_hash(user.password.encode("utf-8"), password)
        print(password, hash_password)
        if hash_password:
            session["username"] = username
            return redirect(url_for("desktop_pages.main_desktop"))
        return render_template("auth/auth.html", form=form)
    return render_template("auth/auth.html", form=form)


@auth_blueprint.route("/out")
def out_page():
    session.clear()
    return redirect(url_for("auth_pages.auth_page"))


@auth_blueprint.route("/delete")
def delete_page():
    user_session = session["username"]
    user_db = db.session.execute(select(User).filter_by(username=user_session)).scalar_one()
    db.session.delete(user_db)
    db.session.commit()
    session.clear()
    return redirect(url_for("auth_pages.auth_page"))