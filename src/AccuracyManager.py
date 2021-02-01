from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
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
        val_confusion_matrix
    ):
        """
        """
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
        """
        """
        y_pred = clf.predict(X)
        y_pred_proba = clf.predict_proba(X)[:, 1]

        clf_score = accuracy_score(y, y_pred)
        clf_f1_score = f1_score(y, y_pred, zero_division=1)
        clf_roc_auc_score = roc_auc_score(y, y_pred_proba)
        clf_confusion_matrix = confusion_matrix(y, y_pred)

        return ClassifierAccuracy(
            clf_score,
            clf_f1_score,
            clf_roc_auc_score,
            clf_confusion_matrix
         )

    def plot_confusion_matrix(
        self,
        clf_acc: ClassifierAccuracy,
        title: str = 'Confusion Matrix'
    ) -> plt:
        """
        """
        labels = ['0', '1']

        ax = plt.subplot()
        sns.heatmap(clf_acc.confusion_matrix, annot=True, ax=ax, fmt=".0f")

        # labels, title and ticks
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.set_title(title)
        ax.xaxis.set_ticklabels(labels)
        ax.yaxis.set_ticklabels(labels)

        return plt
