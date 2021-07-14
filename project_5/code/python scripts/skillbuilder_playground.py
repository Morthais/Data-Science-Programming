#%%
# import packages
import pandas as pd
import altair as alt
import numpy as np

url = "https://byuistats.github.io/CSE250-Larson/skill_builders/munging/munging.csv"

ratings = pd.read_csv(url)

#%%
# display the original dataframe
ratings

#%%
# EXERCISE 0

# %%
# grab the high range value for each movie and put it into a new column
# TODO: call new column high_range_rev from box_office_rev (make sure it is numeric)
# TODO: remove the box_office_rev column from the dataset
# NOTE: .str.split() and .astype() methods may be useful