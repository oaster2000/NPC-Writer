import requests, os, json
from flask import Flask, render_template
from dotenv import load_dotenv
from anvil import Anvil, User

load_dotenv()

app = Flask(__name__)

anvil = Anvil()

user = anvil.load_user()

worlds = anvil.load_worlds(user)

@app.route('/')
def index():
    return render_template('index.html', name=user.name, worlds=worlds)