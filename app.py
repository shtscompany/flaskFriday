import os
from flask import Flask, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app=Flask(__name__)

# Add Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'users.db')}"

app.debug=True
# secret key
app.config['SECRET_KEY']="my Secret  key"

# initialize The Database
db=SQLAlchemy(app)

# #Create model
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    date_added=db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return '<Name %r>' % self.name

# User Form
# Create a Form Class
class UserForm(FlaskForm):
    
    name=StringField("Name", validators=[DataRequired()])
    email=StringField("Email", validators=[DataRequired(), Email(message='Invalid email address.')])
    submit=SubmitField("Submit")

# Create a Form Class
class NamerForm(FlaskForm):
    name=StringField("What's Your Name", validators=[DataRequired()])
    submit=SubmitField("Submit")

@app.route("/user/add", methods=['GET', 'POST'])
def add_user():
    name=None
    form=UserForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user=Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name=form.name.data
        form.name.data=''
        form.email.data=''
        flash('User added succesfuly')
    our_users=Users.query.order_by(Users.date_added)


    return render_template("add_user.html", 
                           form=form,
                           name=name,
                           our_users=our_users)


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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)