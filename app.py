from flask import Flask, render_template, redirect

app=Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return render_template("index.html")

# create Custom Error Pages

# Invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500