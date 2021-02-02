from flask import Flask
from flask import request, render_template
from src.DataManager import DataManager
from src.AccuracyManager import AccuracyManager, ClassifierAccuracy
from src.RFClassifierProvider import RFClassifierProvider

import random
import os

app = Flask(__name__)

"""[Home route]

Returns:
    [View]: [login page]
"""
dataManager = DataManager()
accuracyManager = AccuracyManager()
rfCassifierProvider = RFClassifierProvider()

X_train, y_train, X_test, y_test = dataManager.get_train_test()

# Default model
model = rfCassifierProvider.get_classifier()
model.fit(X_train, y_train)

acc_model_train = accuracyManager.check_model_accuracy(model, X_train, y_train)
acc_model_test = accuracyManager.check_model_accuracy(model, X_test, y_test)

# Hyperparametrized model
model_tuned = rfCassifierProvider.get_classifier(True)
model_tuned.fit(X_train, y_train)

acc_model_tuned_train = accuracyManager.check_model_accuracy(
    model_tuned, X_train, y_train
)
acc_model_tuned_test = accuracyManager.check_model_accuracy(
    model_tuned, X_test, y_test
)


@app.route("/")
@app.route("/home")
def home():
    data = accuracyManager.plot_confusion_matrix(acc_model_train)
    return render_template("home.html", data=data)


@app.route("/tuning", methods=["GET", "POST"])
def tuning():
    data = "tuning"
    # data = somefunction()
    return data


@app.route("/analyse", methods=["GET", "POST"])
def analyse():
    data = "analyse"
    print(data)
    # data = somefunction()
    return data


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
