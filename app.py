# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Create a flask instance
app = Flask(__name__)
# Create Secret Key
app.config['SECRET_KEY'] = 'tsai'

# Create a Form Class
class userform(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def homepage():
    name = None
    form = userform()

    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("name.html",
                           name = name,
                           form = form)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
