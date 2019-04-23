#!/usr/bin/env python

'''metrics.explained_variance_score(y_true, y_pred) 	Explained variance regression score function
metrics.mean_absolute_error(y_true, y_pred) 	Mean absolute error regression loss
metrics.mean_squared_error(y_true, y_pred[, …]) 	Mean squared error regression loss
metrics.mean_squared_log_error(y_true, y_pred) 	Mean squared logarithmic error regression loss
metrics.median_absolute_error(y_true, y_pred) 	Median absolute error regression loss
metrics.r2_score(y_true, y_pred[, …]) 	R^2 (coefficient of determination) regression score function.
'''

from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, mean_squared_log_error, median_absolute_error, r2_score


class MetricReport:
    def __init__(self, y, yhat):
        self.y_true = y
        self.y_pred = yhat
        self.metrics = [explained_variance_score, mean_absolute_error,
                        mean_squared_error, mean_squared_log_error,
                        median_absolute_error, r2_score]
        self.metric_scores = {
            metric: metric(
                y, yhat) for metric in self.metrics}
        self.reports = [
            f"The error {metric.__name__} scored at {self.metric_scores[metric]:.4}" for metric in self.metrics]
        self.show = '\n'.join(self.reports)
