from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hell from Flask App 2'