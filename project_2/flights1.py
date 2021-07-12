#%%
# import packages
import altair as alt
import pandas as pd
import numpy as np

#%%
# from json url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)

# GRAND QUESTION 1
# I chose to define the "worst" delay as the delay with the longest average wait time.
# In my dataframe, the longest wait time is labeled as average_hours. According to this
# definition, the Orlando (ORD) airport has the "worst" delays.

#%%
# What data are we dealing with?
flights.columns

#%%
# Create a new data frame containing all data pertaining to delays.
worst_delays = (flights
    .groupby('airport_code') # group the data by airport to identify delay data for each airport
        .agg(
            flights_total = ('num_of_flights_total', sum), # sum up all flights for each airport
            delays_total = ('num_of_delays_total', sum), # sum up all delays for each airport
            minutes_total = ('minutes_delayed_total', sum) # sum up all minuted delayed for each airport
        )
        .assign(
            percent_delays = lambda x: x.delays_total / x.flights_total,
            average_hours = lambda x: (x.minutes_total / x.delays_total) / 60
        )
    )

worst_delays

#%%
print(worst_delays.to_markdown())

# %%
