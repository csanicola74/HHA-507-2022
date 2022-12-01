from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! This is from a basic flask app - with mods (part3)'