from flask import Flask
from flask import render_template, redirect, request
import json
import os

ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(ROOT, "static/data", "project.json")
PROJECT_DATA = json.load(open(json_url))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/article', methods=['GET'])
def articles():
    return render_template("article.html")

@app.route('/resume', methods=['GET'])
def resume():
    return render_template("resume.html")

@app.route('/whoami', methods=['GET'])
def whoami():
    return render_template("whoami.html")

@app.route('/bin', methods=['GET'])
def bin():
    return render_template("bin.html", data=PROJECT_DATA)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# API Routes
@app.route('/api/projects', methods=['GET'])
def projects():
    json_url = os.path.join(ROOT, "static/data", "project.json")
    data = json.load(open(json_url))
    return data

@app.route('/api/userdata', methods=['GET'])
def userdata():
    json_url = os.path.join(ROOT, "static/data", "userdata.json")
    data = json.load(open(json_url))
    return data

if __name__ == "__main__":
    app.run(debug=True)