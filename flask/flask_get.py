from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/test")
def test():
    return "This is my first function in flask!"

@app.route("/home1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"
@app.route("/home2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route('/hello/<string:name>', defaults={'name': 'world'})
def hello(name):
    return f'Hello, {name}!'


@app.route("/input")
def inp():
    data=request.args.get("x")
    return "this is my input from url {}".format(data)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_info():
    return 'Company Name: ABC Corporation<br>Location: India<br>Contact Detail: 999-999-9999'








if __name__=="__main__":
    app.run(host="0.0.0.0")
