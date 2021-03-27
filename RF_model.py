# -*- coding: utf-8 -*-
"""RF_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h3pZzuJpQEt_aikp9YOSjRgcym5aPQtj

## Random Forest: Fit and evaluate a model

Using the Heart dataset
"""

from time import time
from sklearn.metrics import accuracy_score , precision_score , recall_score

"""### Read in Data"""

import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

dataset = np.loadtxt('./rand_heart.data', delimiter=',')
train = dataset[:,:-1]
label = dataset[:,-1]
tr_features,tst_features = np.split(train,[int(len(train)*0.8)])
tr_labels,tst_labels = np.split(label,[int(len(label)*0.8)])

"""### Hyperparameter tuning


"""

def print_results(results):
    print('BEST PARAMS: {}\n'.format(results.best_params_))

    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))

rf = RandomForestClassifier()
parameters = {
    'n_estimators': [5, 50, 250],
    'max_depth': [2, 4, 8, 16, 32, None]
}

cv = GridSearchCV(rf, parameters, cv=5)
cv.fit(tr_features, tr_labels)

print_results(cv)

"""### Write out pickled model"""

joblib.dump(cv.best_estimator_, './RF_model.pkl')

#Testing
def evaluate_model(name,model,features,labels):
  start = time()
  pred = model.predict(features)
  end = time()
  accuracy = round(accuracy_score(labels,pred),3)
  precision = round(precision_score(labels,pred),3)
  recall = round(recall_score(labels,pred),3)
  print("{} -- accuracy: {} / precision: {} / recall: {} / Latency: {}ms".format(name,accuracy,precision,recall,round((end-start),2)))

model = joblib.load('./RF_model.pkl')

evaluate_model('RF',model,tst_features,tst_labels)

evaluate_model('RF',model,tst_features,tst_labels)