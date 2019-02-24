#Needs flask to be installed
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to my API.</p>"

@app.route('/processText/', methods=['POST'])
def processText():

    print(request.args['text'])

    return "Data returned from model"

#will run in port 5000 by default
app.run()