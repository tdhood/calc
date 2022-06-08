# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.get('/add')
def add_app():
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum = add(a,b)
    return f"Sum of {a} and {b} is {sum}"
