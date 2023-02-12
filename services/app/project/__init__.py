from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='color:black'><center>Hello World!</center></h1>"