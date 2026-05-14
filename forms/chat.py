from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired


class ChatForm(FlaskForm):
    message = StringField(label="Message", validators=[DataRequired(message="Ошибка валидации сообщения")])