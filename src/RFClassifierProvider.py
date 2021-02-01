from sklearn.ensemble import RandomForestClassifier


class RFClassifierProvider:
    """
    This class provides a RandomForestClassifier
    This one can be parametrized or not
    """

    params = {}

    def get_classifier(self, use_params: bool = False) -> RandomForestClassifier:
        """
        This function returns a RandomForestClassifier.
        This one can be set as default or hyperparametrized.

        Params:
        -------
        : use_params bool : If True, the RandomForestClassifier uses
                            the parameters defined in the <params> attributes.
                            Default = False

        Return:
        -------
        : RandomForestClassifier : The RandomForestClassifier
        """

        rf_clf = RandomForestClassifier()

        if use_params:
            rf_clf.set_params(**self.params)

        return rf_clf
