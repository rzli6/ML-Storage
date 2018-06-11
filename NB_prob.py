from sklearn.datasets import make_blobs, make_moons, make_regression, load_iris
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class NaiveBayes(object):
    def __init__(self):
        pass

    def fit(self, X, y):
        separated = [[x for x, t in zip(X, y) if t == c] for c in np.unique(y)]
        total = sum([len(x) for x in separated])
        self.class_prior_ = [len(x) / total for x in separated]
        self.class_count_ = len(separated)
        self.model = np.array([np.c_[np.mean(i, axis=0), np.std(i, axis=0)] for i in separated])
        return self
    
    def _prob(self, x, mean, std):
        exponent = np.exp(- ((x - mean)**2 / (2 * std**2)))
        return np.log(exponent / (np.sqrt(2 * np.pi) * std))
    
    def predict_log_proba(self, X):
        prob = [[sum(self._prob(i, *s) for s, i in zip(summaries, x)) for summaries in self.model] for x in X]
        result = [[x[i] +  np.log(self.class_prior_)[i] for i in range(0, self.class_count_)] for x in prob]
        return result
    
    def predict(self, X):
        result = np.argmax(self.predict_log_proba(X), axis=1)
        return result
    
    def prob(self, X):
        result = np.max(self.predict_log)