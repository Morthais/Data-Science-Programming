#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import tree

#%%
# import all data
dwellings_denver_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'
dwellings_ml_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv'
dwellings_neighborhoods_ml_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv'

dwellings_denver = pd.read_csv(dwellings_denver_url)
dwellings_ml = pd.read_csv(dwellings_ml_url)
dwellings_neighborhoods_ml = pd.read_csv(dwellings_neighborhoods_ml_url)

# GRAND QUESTION 2
#%%
'''
CLASSIFICATION MODEL 2 (RandomForestClassifier)
FINAL MODEL CHOICE
'''

#%%
# SPLIT the dwellings_ml data into features and targets numpy arrays
# (if features include 'yrbuilt' then accuracy is 1.0 / 1.0 or 100%)
# (without 'yrbuilt', accuracy is 0.938 / 1.0 or 93.8%)
features = dwellings_ml.filter(
    ['sprice','stories','nocars',
    'livearea','basement','numbaths', 
    'numbdrm','arcstyle_END UNIT','arcstyle_MIDDLE UNIT',
    'arcstyle_ONE AND HALF-STORY','arcstyle_ONE-STORY','arcstyle_TWO-STORY',
    'status_I','gartype_Det','gartype_Att',
    'quality_C','quality_B','condition_Good',
    'condition_AVG','deduct','totunits',
    'finbsmnt','abstrprd']
    ).to_numpy()
targets = dwellings_ml.filter(['before1980']).to_numpy()

# SPLIT the data into training and testing variables
# TODO: tinker with the split to see if input attributes impact accuracy
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=.3, random_state=24, stratify=None)

# TRAIN the classifier model
# fit the classifier with the training data
# NOTE: why does targets_train request use of .ravel()?
classifier = RandomForestClassifier(random_state=42)
classifier.fit(features_train, targets_train.ravel())

# TEST the classifier with a prediction using the test features
predictions = classifier.predict(features_test)

# COMPARE target_predictions with the actual values (targets_test)
metrics.accuracy_score(predictions, targets_test)

# GRAND QUESTION 3

# %%
# PLOT FEATURE IMPORTANCE
feature_df = pd.DataFrame({'features':features.columns, 'importance':classifier.feature_importances_})
feature_df

feature_chart = alt.Chart(feature_df).mark_bar().encode(
    x = ('importance'),
    y = alt.Y('features', sort='-x')
)

feature_chart.save('Images/ImportantFeatures_Before1980.png')

# GRAND QUESTION 4

#%%
# print a matrix showing evaluation metrics?
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

# %%
