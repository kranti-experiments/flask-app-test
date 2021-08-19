from flask import Flask, render_template
from forms import UserForm

#Create a flask instance
app = Flask(__name__)
# Create Secret Key
app.config['SECRET_KEY'] = 'tsai'


@app.route('/', methods=['GET', 'POST'])
def homepage():
    name = None
    form = UserForm()

    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("user.html",
                           name = name,
                           form = form)

if __name__ == '__main__':
    app.run(debug=True)
