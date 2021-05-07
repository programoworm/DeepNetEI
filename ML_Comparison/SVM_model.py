# -*- coding: utf-8 -*-
"""SVM_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FGbFKelJX9M9lSMgPSU2kSVZS-QeaXlF

## Support Vector Machines: Fit and evaluate a model

Using the Heart dataset

### Read in Data
"""

from time import time
from sklearn.metrics import accuracy_score , precision_score , recall_score

import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
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

svc = SVC()
parameters = {
    'kernel': ['linear', 'rbf'],
    'C': [0.1, 1, 10]
}

cv = GridSearchCV(svc, parameters, cv=5)
cv.fit(tr_features, tr_labels)

print_results(cv)

cv.best_estimator_

"""### Write out pickled model"""

joblib.dump(cv.best_estimator_, './SVM_model.pkl')

#Testing
def evaluate_model(name,model,features,labels):
  start = time()
  pred = model.predict(features)
  end = time()
  accuracy = round(accuracy_score(labels,pred),3)
  precision = round(precision_score(labels,pred),3)
  recall = round(recall_score(labels,pred),3)
  print("{} -- accuracy: {} / precision: {} / recall: {} / Latency: {}ms".format(name,accuracy,precision,recall,round((end-start),2)))

model = joblib.load('./SVM_model.pkl')

evaluate_model('SVM',model,tst_features,tst_labels)