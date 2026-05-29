from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ChatForm(FlaskForm):
    message = StringField(label="Message", validators=[DataRequired(message="Ошибка валидации сообщения")])