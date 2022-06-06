from flask import Flask
from flask import request
from flask import jsonify
from flask import json


app= Flask(__name__)

@app.route("/")
def get_saw():
  return "<h1>Welcome to Adaptive Speech</h1>"  
@app.route("/get_yaw")
def get_yaw():
  return "<h1>Yaaaaaw</h1>"  
@app.route("/hel")
def maw():
  return "<h1>Helloooooo</h1>"  


if __name__ == '__main__':
    app.run(debug=True)
