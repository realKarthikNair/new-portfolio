from flask import Flask
from flask import render_template, redirect, request

import json

with open("~/portfolio/static/data/project.json", "r") as f:
    PROJECT_DATA = json.load(f)

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

if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run()