from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "This is a test to route Flask and Python :)"

@app.route('/ninjas')
def ninjas():
    return render_template('index.html', ninja_turtles = True)

@app.route('/ninjas/<ninja_color>')
def color(ninja_color):
    return render_template('index.html', ninja_turtles = False, color = ninja_color)
