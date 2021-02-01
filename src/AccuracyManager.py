from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    roc_curve,
)
import matplotlib.pyplot as plt
import seaborn as sns


class ClassifierAccuracy:
    """
    This class represents a Classifier Accuracy
    """

    score: float = None
    f1_score: float = None
    roc_auc_score: float = None
    confusion_matrix = None

    def __init__(
        self,
        val_score: float,
        val_f1_score: float,
        val_roc_auc_score: float,
        val_confusion_matrix,
    ):
        """"""
        self.score = val_score
        self.f1_score = val_f1_score
        self.roc_auc_score = val_roc_auc_score
        self.confusion_matrix = val_confusion_matrix


class AccuracyManager:
    """
    This class allows you to test the accuracy of your
    classification model.
    """

    def check_model_accuracy(self, clf, X, y) -> ClassifierAccuracy:
        """"""
        y_pred = clf.predict(X)
        y_pred_proba = clf.predict_proba(X)[:, 1]

        clf_score = accuracy_score(y, y_pred)
        clf_f1_score = f1_score(y, y_pred, zero_division=1)
        clf_roc_auc_score = roc_auc_score(y, y_pred_proba)
        clf_confusion_matrix = confusion_matrix(y, y_pred)

        return ClassifierAccuracy(
            clf_score, clf_f1_score, clf_roc_auc_score, clf_confusion_matrix
        )

    def plot_confusion_matrix(
        self, clf_acc: ClassifierAccuracy, title: str = "Confusion Matrix"
    ) -> plt:
        """"""
        labels = ["0", "1"]
        ax = plt.subplot()
        sns.heatmap(clf_acc.confusion_matrix, annot=True, ax=ax, fmt=".0f")

        # labels, title and ticks
        ax.set_xlabel("Predicted labels")
        ax.set_ylabel("True labels")
        ax.set_title(title)
        ax.xaxis.set_ticklabels(labels)
        ax.yaxis.set_ticklabels(labels)
        plt.fig_to_html()

        return plt

    def get_roc_curve(self, clf, X, y):
        """"""
        y_pred_proba = clf.predict_proba(X)[::, 1]
        fpr, tpr, _ = roc_curve(y, y_pred_proba)
        return fpr, tpr

    def plot_roc_curve(self, clf, X, y) -> plt:
        """"""
        fpr, tpr = self.get_roc_curve(clf, X, y)

        plt.plot(fpr, tpr, color="orange", label="ROC")
        plt.plot([0, 1], [0, 1], color="darkblue", linestyle="--")

        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("Receiver Operating Characteristic (ROC) Curve")
        plt.legend()

        return plt

    def plot_roc_curves(
        self, clf_1, X_1, y_1, clf_2, X_2, y_2, label_1="ROC 1", label_2="ROC 2"
    ) -> plt:
        """"""
        fpr, tpr = self.get_roc_curve(clf_1, X_1, y_1)
        plt.plot(fpr, tpr, color="orange", label=label_1)

        fpr, tpr = self.get_roc_curve(clf_2, X_2, y_2)
        plt.plot(fpr, tpr, color="orange", label=label_2)
        plt.plot([0, 1], [0, 1], color="darkblue", linestyle="--")

        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("Receiver Operating Characteristic (ROC) Curve")
        plt.legend()

        return plt
