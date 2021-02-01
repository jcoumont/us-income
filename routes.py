from flask import Flask
from flask import Flask, request, render_template
from src.DataManager import DataManager
from src.AccuracyManager import AccuracyManager
from src.RFClassifierProvider import RFClassifierProvider
import random
import os

app = Flask(__name__)

"""[Home route]

Returns:
    [View]: [login page]
"""
dataManager = DataManager()
accuracyManager = AccuracyManager ()
rfCassifierProvider = RFClassifierProvider()
X_train,y_train,X_test,y_test = dataManager.get_train_test()
model = rfCassifierProvider.get_classifier()
@app.route("/")
@app.route("/home")
def home():
    data = accuracyManager.plot_confusion_matrix(model,X_train,y_train)
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
