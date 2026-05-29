from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TerminalForm(FlaskForm):
    comand = StringField(label="Comand", validators=[DataRequired(message="Ошибка валидации команды")])