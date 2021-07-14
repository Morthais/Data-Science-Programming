#%%
# import packages
import pandas as pd
import altair as alt
import numpy as np

#%%
# import url
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'
starwars = pd.read_csv(url)

#%%
# WARNING: utf-8 ENCODING DOES NOT WORK
starwars = pd.read_csv(url, encoding="utf-8")

#%%
# NOTE: ISO-8859-1 ENCODING DOES WORK
starwars = pd.read_csv(url, encoding="ISO-8859-1")
