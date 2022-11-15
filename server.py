from typing import no_type_check
import joblib
import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Are you sure? Aguante Racing</p>"

if __name__== "__main__":
    app.run(port=8000,debug=True)