#%%
# import packages
import pandas as pd
import altair as alt
import numpy as np

#%%
# import data
url = "https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv"

starwars = pd.read_csv(url)
starwars