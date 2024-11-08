from flask import Flask, render_template

# Create a Flaske Instance

app= Flask(__name__)

# create a route decoratior

# @app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

@app.route("/")
def index():
    return render_template("index.html")


#localhosr:5000/user/shota
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello World! {}</h1>".format(name)
