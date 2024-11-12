from flask import Flask, render_template, redirect

app=Flask(__name__)
app.debug=True

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