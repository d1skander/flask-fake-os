from flask import Flask
from flask_wtf.csrf import CSRFProtect
from auth.auth import auth_blueprint
from dotenv import load_dotenv
from os import getenv


load_dotenv()


app =  Flask(__name__)
csrf=CSRFProtect(app)
app.secret_key = getenv("SECRET_KEY")


app.register_blueprint(auth_blueprint, url_prefix="/auth")


if __name__ == "__main__":
    app.run(debug=True, port=7272)