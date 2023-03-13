import requests, os, json
from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from anvil import Anvil, User

load_dotenv()

app = Flask(__name__)
anvil = Anvil()
user = anvil.load_user()
worlds = anvil.load_worlds(user)
anvil.current_world = worlds[0]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        anvil.current_world = anvil.get_world(worlds, request.form["world"])
        
    return render_template('index.html', name=user.name, worlds=worlds, current_world=anvil.current_world)


@app.route('/new_article', methods=['POST', 'GET'])
def new_article():
    if request.method == 'POST':
        return redirect(url_for("/"))
        
    return render_template('new_article.html', name=user.name, worlds=worlds, current_world=anvil.current_world)

if __name__ == "__main__":
    app.run(debug=True)