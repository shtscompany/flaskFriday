from flask import Flask, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.debug=True

app.config['SECRET_KEY']="my Secret  key"
# Create a Form Class
class NamerForm(FlaskForm):
    name=StringField("What's Your Name", validators=[DataRequired()])
    submit=SubmitField("Submit")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/')
def index():
    first_name="John Tsiklauri"
    stuff="this is the <strong>bold<strong> tag"
    favorite_pizza=["Pepparony", "cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


# Crete Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name=None
    form=NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash("Form Submitted Successfully")
    return render_template('name.html',
                           name = name,
                           form = form)