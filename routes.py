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

data = []


@app.route("/")
@app.route("/home")
def home():
    # confusion_matrix = accuracyManager.plot_confusion_matrix(acc_model_train)
    # roc_curves = accuracyManager.plot_roc_curves(model_tuned, X_train, y_train, model_tuned, X_test, y_test, 'Roc train', 'Roc test')
    # data.append(confusion_matrix)
    # data.append(roc_curves)
    data = {
        "acc_model_train": acc_model_train,
        "acc_model_test": acc_model_test
    }
    return render_template("home.html", data=data)


@app.route("/tuning")
def tuning():
    roc_curve_default = accuracyManager.plot_roc_curves(model,X_train,y_train,model,X_test,y_test,'Roc train','Roc test')
    roc_curve_tuned = accuracyManager.plot_roc_curves(model_tuned,X_train,y_train,model_tuned,X_test,y_test,'Roc train','Roc test')
    graphs.append(roc_curve_default)
    graphs.append(roc_curve_tuned)
    default_params = model.get_params()
    tuned_params = model_tuned.get_params()
    return render_template("tuning.html", graphs = graphs,default=default_params,tuned=tuned_params)


@app.route("/analyse")
def analyse():
    data = {}
    # data = somefunction()
    return render_template("analyse.html", data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
