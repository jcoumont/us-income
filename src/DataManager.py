import pandas as pd


class DataManager:
    """
    The DataManager helps you to deal with the datas.

    Attributes
    ----------
    :train_file  str: path of the train dataset.
    :test_file   str: path of the test dataset.
    :target_name str: name of the target column.
    """

    train_file: str = "../data/data_train.csv"
    test_file: str = "../data/data_test.csv"
    target_name: str = "income"

    def get_X_y(self, file_path: str) -> (pd.Series, pd.Series):
        """
        This fuction returns the features and the target from
        a specified file.

        Parameters
        ----------
        :file_path str: path of the dataset to extract features and target

        Return
        ------
        : X : the features
        : y : the target
        """
        df = pd.read_csv(file_path)
        X = df.drop(self.target_name, axis=1)
        y = df[self.target_name]

        return X, y

    def get_train_test(self) -> (pd.Series, pd.Series, pd.Series, pd.Series):
        """
        This fuction returns the features and the target from
        the train and test files.

        Parameters
        ----------
        None

        Return
        ------
        : X_train : the features from the train file
        : y_train : the target from the train file
        : X_test  : the features from the test file
        : y_test  : the target from the test file
        """
        X_train, y_train = self.get_X_y(self.train_file)
        X_test, y_test = self.get_X_y(self.test_file)
        return X_train, y_train, X_test, y_test
