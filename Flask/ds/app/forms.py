from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError


class ContactForm(Form):
    name = StringField('Imię i nazwisko', validators=[DataRequired()])
    email = StringField('Twój adres e-mail', validators=[DataRequired()])
    subject = StringField('Temat')
    message = TextAreaField("Wiadomość", validators=[DataRequired()])
    submit = SubmitField('Wyślij')