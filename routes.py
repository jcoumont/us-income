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
    data = "test"
    # data = somefunction()
    return render_template("home.html", data=data)


@app.route("/tuning",methods=["GET", "POST"])
def tuning():
    data = 'tuning'
    #data = somefunction()
    return data


@app.route("/analyse",methods=["GET", "POST"])
def analyse():
    data = 'analyse'
    print(data)
    #data = somefunction()
    return data


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
