import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

dataset = np.loadtxt('./Datasets/rand_heart.data', delimiter=',')
train = dataset[:,:-1]
label = dataset[:,-1]
tr_features,tst_features = np.split(train,[int(len(train)*0.8)])
tr_labels,tst_labels = np.split(label,[int(len(label)*0.8)])



tr_features

tr_labels[:5]

tr_features = pd.DataFrame(tr_features)

tr_features



def print_results(results):
    print('BEST PARAMS: {}\n'.format(results.best_params_))

    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))

mlp = MLPClassifier()
parameters = {
    'hidden_layer_sizes': [(100,),(200,),(250),(270,)],
    'activation': ['relu','tanh','logistic'],
    'learning_rate': ['constant','invscaling','adaptive']
}
cv = GridSearchCV(mlp,parameters,cv=5)
cv.fit(tr_features,tr_labels) #.values.ravel())
print_results(cv)

cv.best_estimator_

joblib.dump(cv.best_estimator_,'./MLP_Model.pkl')