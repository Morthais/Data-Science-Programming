#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#%%
# import data
titanic = pd.read_csv('https://byuistats.github.io/CSE250-Larson/skill_builders/ml_sklearn/machine_learning.csv')

#%%
# understand the data
titanic.head()

#%%
# create modified dataframe for chart
# calculate the density (sum of each age)
titanic_modified = (titanic
    .groupby('age')
        .agg(
            count_of_age = ('age', sum)
        )
        .assign(
            density = lambda x: x.count_of_age * .001
        )
        .filter(
            ['survived']
        )
)

# %%
alt.Chart(titanic_modified).mark_bar().encode(
    x = 'age:O',
    y = 'density'
).properties(
    title = {
        "text":"Does age affect whether a passenger survived?",
    }
)
# %%
