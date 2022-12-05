from flask import Flask

app = Flask(__name__)

equaiton = 5 + 5 

@app.route('/')
def hello():
    return 'Hello World form a docker-compose environment {} !!!!! ! '.format(equaiton)