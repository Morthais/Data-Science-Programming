#%%
# import packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#%%
# load data
url = "https://byuistats.github.io/CSE250-Larson/course-materials/machine-learning/iris.csv"
data = pd.read_csv(url)

'''
BUILD A CLASSIFIER ALGORITHM
Question: Can classify data about a flower as the correct flower without knowing the flower?
'''
#%%
# split the data into two numpy arrays (so that sklearn can process the arrays)
# select the feature columns ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
features = data.filter(['sepal_length', 'sepal_width', 'petal_length', 'petal_width']).to_numpy()
# select the targets column ('species')
targets = data.filter(['species']).to_numpy()
print("\nFeatures Array\n", features)
print("\nTargets Array\n", targets)

#%%
# Randomize and split the samples into two groups of arrays (train_test_split()).
# The method creates two groups of arrays: features and targets, each with two arrays;
# One of those arrays is for training (70% of the dataframe in this case);
# The other array is for testing (30% of the dataframe in this case).
# NOTE: For train_test_split, the training arrays get the remainder of the sample (1 - .3 = .7).
# trainX, testX, trainY, testY... is how train_test_split decides where to put the data
train_features, test_features, train_targets, test_targets = train_test_split(features, targets, test_size=.3)

#%%
print(train_features)
#%%
print(test_features)
#%%
print(test_targets)
#%%
print(train_targets)

#%%
# TRAIN a classifier
# specify which algorithm to use in predictions
classifier = GaussianNB()
# telling the algorithm "look at these dataframes"
# "these are the features for these flowers"
# (uses 70% of the original dataframe)
classifier.fit(train_features, train_targets)

#%%
# TEST the classifier
# telling the algorithm "look at this dataframe"
# "use these features to predict their flowers"
# checks 30% of the original data
targets_predicted = classifier.predict(test_features)
print(targets_predicted)

#%%
# ASSESS classifier performance
# this method takes the predictions given by the algorithm and compares them with the actual dataframe
# then spits out a confidence/probability of accuracy number between 0 and 1 (1 is 100% accuracy)
# NOTE: figure out how this method actually works
accuracy_score(targets_predicted, test_targets, normalize=True)

# %%
