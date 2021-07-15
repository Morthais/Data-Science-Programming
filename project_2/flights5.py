#%%
# import packages
import pandas as pd
import numpy as np
import json

#%%
# from json url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)

# GRAND QUESTION 5

#%%
flights.isnull().sum()

#%%
# Fix all of the varied missing data types in the data to be consistent
# (all missing values should be displayed as "NaN") and save the new data
# as a JSON file.

# columns with missing data: airport_name (empty cells), month (n/a), year (nan), num_of_delays_late_aircraft (-999), 
# minutes_delayed_carrier (nan), minutes_delayed_nas (nan AND -999)

# Reformat the missing values
flights_new = flights.replace('', np.nan).replace('n/a', np.nan).replace(-999, np.nan).replace('null', np.nan)

# %%
# Compare with the original to ensure the reformat worked
flights.isnull().sum()

#%%
# Did the reformat work?
# If the system detects more null cells, Yes!
flights_new.isnull().sum()

#%%
# by table
json_data = flights_new.to_json(orient="table")
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)

#%%
# by record or row
json_data = flights_new.to_json(orient="records")
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)

# %%
