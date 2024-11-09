from flask import Flask, render_template
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# create a flask instance
app=Flask(__name__)

# create a route decorator

@app.route('/')
def index():
    first_name="John Tsiklauri"
    stuff="this is the <strong>bold<strong> tag"
    favorite_pizza=["Pepparony", "cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)
# FILTERS
# '''
# safe
# capitalize
# upper
# title
# trim
# striptags
# '''
    
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


if __name__=="__main__":
    app.run(debub=True)