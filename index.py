import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import html

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else
  with open('data.json') as json_data:
    data = json.load(json_data)
    print(data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    return jsonify(data)
app.run(host='localhost', debug=True)