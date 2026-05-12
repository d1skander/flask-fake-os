from flask import Flask, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from auth.auth import auth_blueprint
from desktop.desktop import desktop_blueprint
from dotenv import load_dotenv
from os import getenv
from models.user import db
from admin.admin import admin_setup
from flask_babel import Babel


load_dotenv()


app =  Flask(__name__)
babel=Babel(app)
csrf=CSRFProtect(app)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)


app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(desktop_blueprint, url_prefix="/desktop")


@app.route("/")
def redirect_user():
    return redirect(url_for("auth_pages.registration_page"))


def create_db():
    with app.app_context():
        db.create_all()


admin_setup(app)


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=7272)