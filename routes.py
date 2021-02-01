from flask import Flask
from flask import Flask, request, render_template
import random
import os

app = Flask(__name__)

"""[Home route]

Returns:
    [View]: [login page]
"""


@app.route("/")
@app.route("/home")
def home():
    data = 'test'
    #data = somefunction()
    return render_template("home.html", data=data)


@app.route("/tuning")
def tuning():
    data = 'test'
    #data = somefunction()
    return render_template("tuning.html", data=data)


@app.route("/analyse")
def analyse():
    data = 'test'
    #data = somefunction()
    return render_template("analyse.html", data=data)
s
if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
