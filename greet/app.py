from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
   return f"Welcome"


@app.route('/welcome/home')
def welcome_home():
   return f"Welcome Home"


@app.route('/welcome/back')
def welcome_back():
   return f"Welcome Back"