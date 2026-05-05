from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(message="Ошибка валидации имени")])
    email = EmailField(label="Email", validators=[DataRequired(message="Ошибка валидации почты")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Ошибка валидации пароля")])

class AuthForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(message="Ошибка валидации имени")])
    password = PasswordField(label="Password", validators=[DataRequired(message="Ошибка валидации пароля")])