from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField("What's Your Name ?!", validators=[DataRequired()])
    submit = SubmitField("Test")