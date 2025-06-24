import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello_world():
    secret = os.getenv("SECRET_VARIABLE", "none")
    print('Github')
    return f"<p>Hello, World! with secret {secret}</p>"