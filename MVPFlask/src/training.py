#!/usr/bin/env python

import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from .clean import Data, PTHURL
from .metric_report import MetricReport
#from .utils import Spinner
#spin = Spinner()

dat = Data(PTHURL)
X = dat.X
y = dat.y

'''
class GBR:

    def __init__(self, X: pd.DataFrame = X, y: pd.DataFrame = y):
        from xgboost import train as Train, DMatrix
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y)
        self.dtrain = DMatrix(self.X_train.values, self.y_train.values)
        self.dtest = DMatrix(self.X_test.values)

        self.feat_names_mapper = {
            ident: name for ident, name in zip(
                self.dtrain.feature_names, X.columns)}

        self.params = {
            'objective': 'reg:linear',
            'max_depth': 3,
            'learning_rate': 0.1,
            'n_estimators': 100,
            'silent': 1}
        self.num_round = 2
        self.model = Train(self.params, self.dtrain, self.num_round)
        self.prediction = self.model.predict(self.dtest)

'''


class RFR:
    def __init__(self, X: pd.DataFrame = X, y: pd.DataFrame = y):
        from sklearn.ensemble import RandomForestRegressor
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y)
        self.model = RandomForestRegressor(n_estimators=100)
        self.model.fit(self.X_train, self.y_train)
        self.prediction = self.model.predict(self.X_test)


# spin.start()
#gbr = GBR(X, y)

rfr = RFR(X, y)

REPORTS = {
    # 'gradient boost performance': MetricReport(
    #        gbr.y_test.values,
    #        gbr.prediction).show#,
    'random forest performance': MetricReport(
        rfr.y_test,
        rfr.prediction).show}

# spin.stop()
