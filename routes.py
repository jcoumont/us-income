from flask import Flask
from flask import jsonify, render_template
from src.DataManager import DataManager
from src.AccuracyManager import AccuracyManager
from src.RFClassifierProvider import RFClassifierProvider

import random
import os

app = Flask(__name__)

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

data = []


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html",
        train_score=acc_model_train.score,
        train_f1=acc_model_train.f1_score,
        train_roc_auc=acc_model_train.roc_auc_score,
        test_score=acc_model_test.score,
        test_f1=acc_model_test.f1_score,
        test_roc_auc=acc_model_test.roc_auc_score
        )


@app.route("/tuning")
def tuning():
    default_params = model.get_params()
    tuned_params = model_tuned.get_params()
    return render_template(
        "tuning.html",
        default=default_params,
        tuned=tuned_params)


@app.route("/analyse")
def analyse():
    data = {}
    return render_template("analyse.html", data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
