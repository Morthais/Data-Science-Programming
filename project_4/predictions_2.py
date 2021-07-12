# SUPERVISED MACHINE LEARNING

# EXERCISE 2
# Predict whether a house was built before1980.

#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import catboost as cb # CatBoostClassifier
from sklearn import metrics

#%%
# import all data
dwellings_denver_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'
dwellings_ml_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv'
dwellings_neighborhoods_ml_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv'

dwellings_denver = pd.read_csv(dwellings_denver_url)
dwellings_ml = pd.read_csv(dwellings_ml_url)
dwellings_neighborhoods_ml = pd.read_csv(dwellings_neighborhoods_ml_url)

#%%
dwellings_ml.describe()  # Summary statistics

#%%
'''
CLASSIFICATION MODEL 1 (GaussianNB)
'''

#%%
# SPLIT the dwellings_ml data into features and targets numpy arrays
# could also use .remove() to include everything except chosen features
features = dwellings_ml.filter(['sprice'])
targets = dwellings_ml.filter(['before1980'])

#%%
# SPLIT the data into training and testing variables
# TODO: tinker with the split to see if attributes impact accuracy
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=.34, random_state=76, stratify=targets)

print(np.average(targets_test.head(10)))
#%%
# FIT (or train) the classifier model
# fit the classifier with the training data
# NOTE: why does targets_train request use of .ravel()?
classifier = GaussianNB()
classifier.fit(features_train, targets_train.ravel())

#%%
# TEST the classifier with a prediction using the test features
# in other words, guess which dwellings were built before1980 using these features
predictions = classifier.predict(features_test)

#%%
# COMPARE target_predictions with the actual values (targets_test)
metrics.accuracy_score(predictions, targets_test)

#%%
# print a matrix showing true and false predictions
# We want the top left and bottom right to be high (true predictions)
# We want the top right and bottom left to be low (false predictions)
print(metrics.confusion_matrix(targets_test, predictions))
#%%
# this matrix may be easier to read
print(pd.crosstab(targets_test.flatten(), predictions, rownames=['True'], colnames=['Predicted'], margins=True))

#%%
# print a matrix including RECALL, PRECISION, F1-SCORE
# best way to evaluate a model (provides all evaluation metrics)
# includes accuracy score, precision, recall, f1-score, and total predictions made
# (0 is negative predictions, 1 is positive predictions)
print(metrics.classification_report(targets_test, predictions))

# RECALL: The number of times you didn't get it right. (low is bad)
# PRECISION: The number of time you did get it right. (low is bad)
# F1-SCORE: The mean of PRECISION and RECALL

#%%
# visualize a confusion matrix
metrics.plot_confusion_matrix(classifier, features_test, targets_test)

#%%
'''
CLASSIFICATION MODEL 2 (RandomForestClassifier)
FINAL MODEL CHOICE
'''

#%%
# SPLIT the dwellings_ml data into features and targets numpy arrays
features = dwellings_ml.filter(
    ['sprice','stories','nocars',
    'livearea','basement','numbaths', 
    'numbdrm','totunits', 'arcstyle_SPLIT LEVEL']
    ).to_numpy()
targets = dwellings_ml.filter(['before1980']).to_numpy()

# SPLIT the data into training and testing variables
# TODO: tinker with the split to see if input attributes impact accuracy
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=.3, random_state=24, stratify=None)

# TRAIN the classifier model
# fit the classifier with the training data
# NOTE: why does targets_train request use of .ravel()?
classifier = RandomForestClassifier(random_state=24)
classifier.fit(features_train, targets_train.ravel())

# TEST the classifier with a prediction using the test features
targets_predictions = classifier.predict(features_test)

#%%
# COMPARE target_predictions with the actual values (targets_test)
metrics.accuracy_score(targets_predictions, targets_test)

#%%
# print a matrix showing evaluation metrics?
print(metrics.confusion_matrix(targets_test, predictions))

#%%
'''
CLASSIFICATION MODEL 3 (DecisionTreeClassifier)
'''

#%%
# RUN the DecisionTreeClassifier

# SPLIT the data into features and targets numpy arrays
features = dwellings_ml.filter(
    ['sprice','stories','nocars',
    'livearea','basement','numbaths', 
    'numbdrm','totunits', 'arcstyle_SPLIT LEVEL']
    )
targets = dwellings_ml.filter(['before1980'])

# SPLIT the data into training and testing variables
# TODO: tinker with the split to see if input attributes impact accuracy
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=.3, random_state=42, stratify=None)

# TRAIN the classifier model
# fit the classifier with the training data
# NOTE: why does targets_train request use of .ravel()?
classifier = DecisionTreeClassifier()
classifier.fit(features_train, targets_train)

# TEST the classifier with a prediction using the test features
predictions = classifier.predict(features_test)

#%%
# EVALUATE THE MODEL
# COMPARE target_predictions with the actual values (targets_test)
metrics.accuracy_score(predictions, targets_test)
#%%
# print a matrix showing true and false predictions
# We want the top left and bottom right to be high (true predictions)
# We want the top right and bottom left to be low (false predictions)
print(metrics.confusion_matrix(targets_test, predictions))

#%%
'''
CLASSIFICATION MODEL 4 (GradientBoostingClassifier)
'''

#%%
# RUN the GradientBoostingClassifier

# SPLIT the dwellings_ml data into features and targets numpy arrays
features = dwellings_ml.filter(
    ['sprice','stories','nocars',
    'livearea','basement','numbaths', 
    'numbdrm','totunits', 'arcstyle_SPLIT LEVEL']
    ).to_numpy()
targets = dwellings_ml.filter(['before1980']).to_numpy()

# SPLIT the data into training and testing variables
# TODO: tinker with the split to see if input attributes impact accuracy
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=.3, random_state=42, stratify=None)

# TRAIN the classifier model
# fit the classifier with the training data
# NOTE: why does targets_train request use of .ravel()?
classifier = GradientBoostingClassifier(random_state=42)
classifier.fit(features_train, targets_train.ravel())

# TEST the classifier with a prediction using the test features
targets_predictions = classifier.predict(features_test)

#%%
# COMPARE target_predictions with the actual values (targets_test)
metrics.accuracy_score(targets_predictions, targets_test)

#%%
# print a matrix showing evaluation metrics?
print(metrics.confusion_matrix(targets_test, predictions))

#%%
'''
CLASSIFICATION MODEL 5 (CatBoostClassifier)
'''

#%%
# RUN the CatBoostClassifier

# SPLIT the dwellings_ml data into features and targets numpy arrays
features = dwellings_ml.filter(
    ['sprice','stories','nocars',
    'livearea','basement','numbaths', 
    'numbdrm','totunits', 'arcstyle_SPLIT LEVEL']
    ).to_numpy()
targets = dwellings_ml.filter(['before1980']).to_numpy()

# SPLIT the data into training and testing variables
# TODO: tinker with the split to see if input attributes impact accuracy
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=.3, random_state=42, stratify=None)

# TRAIN the classifier model
# fit the classifier with the training data
# NOTE: why does targets_train request use of .ravel()?
classifier = cb.CatBoostClassifier(iterations=10,
                           depth=6,
                           learning_rate=1,
                           loss_function='Logloss',
                           verbose=False)
classifier.fit(features_train, targets_train)

# TEST the classifier with a prediction using the test features
predictions = classifier.predict(features_test)

#%%
# COMPARE target_predictions with the actual values (targets_test)
metrics.accuracy_score(predictions, targets_test)

#%%
# print a matrix showing evaluation metrics?
print(metrics.confusion_matrix(targets_test, predictions))
# %%
