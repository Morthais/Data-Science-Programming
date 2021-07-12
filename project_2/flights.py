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

#%%
# What data are we dealing with?
flights.columns

#%%
# Create a new data frame containing all data pertaining to delays.
# Ask yourself which columns are related to airport delays in general,
# Think of what data would be nice to have to determine which airport has the worst delays,
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

# GRAND QUESTION 2

#%%
# What data are we dealing with?
flights.shape

# %%
# Create a new data frame containing all data pertaining to delays, 
# but group by month instead of by airport.
best_months = (flights
    .groupby('month')
        .agg(
            flights_total = ('num_of_flights_total', sum),
            delays_total = ('num_of_delays_total', sum),
            minutes_total = ('minutes_delayed_total', sum)
        )
        .assign(
            percent_delays = lambda x: x.delays_total / x.flights_total,
            average_hours = lambda x: x.minutes_total / x.delays_total / 60
        )
        .reset_index()
        .drop(labels=12, axis=0)
    )

best_months

# %%
chart = alt.Chart(best_months).encode(
    x = 'month',
    y = 'average_hours'
).mark_bar()

chart

# GRAND QUESTION 3

#%%
# What data are we dealing with?
flights.columns

#%%
# GOAL: Calculate total number of flights delayed by weather
# TODO: Calculate 30% of late-arriving aircraft for mild weather delays
# TODO: Calculate 40% of delayed flights in NAS from April to August, 
# TODO: Calculate 65% of delayed flights in NAS from September to March.
#flights.replace("num_of_delays_late_aircraft", NaN, )

weather_delays = (flights
    .assign(
        # select all missing values in num_of_delays_late_aircraft and replace with the mean
        severe = lambda x: x.num_of_delays_weather.replace(-999, x.num_of_delays_weather.mean()),
        # calculate 30% of late-arriving aircraft to find some mild weather delays
        mild_late = lambda x: x.num_of_delays_late_aircraft * .30,
        # sum all values in the nas column from April to August and multiply by .40
        mild_nas = lambda x: np.where(
            x.month.isin(["April", "May", "June", "July", "August"]),
            x.num_of_delays_nas * .40,
            x.num_of_delays_nas * .65),

        total_weather = lambda x: x.severe + x.mild_late + x.mild_nas,
        total_late = lambda x: x.num_of_delays_weather + x.num_of_delays_late_aircraft + x.num_of_delays_nas,
        percent_weather = lambda x: x.total_weather / x.total_late,
    )
    .filter(
        ['airport_code', 'month', 'severe','mild_late','mild_nas', 'total_weather', 'total_late', 'percent_weather']
    )
)

weather_delays

# GRAND QUESTION 4
# This chart shows that the Atlanta airport has the worst ratio of delays caused by weather, meaning we can
# expect the majority of delays have to do with weather for flights involving the Atlanta airport.

#%%
# create a barplot showing the proportion of all flights delayed by weather at each airport
weather_chart = alt.Chart(weather_delays).encode(
    x = alt.X('airport_code', axis=alt.Axis(title='Airport Code')),
    y = alt.Y('percent_weather', axis=alt.Axis(format="%", title='Proportion of Flights Delayed by Weather'))
).mark_bar()

weather_chart

# GRAND QUESTION 5

#%%
# Fix all of the varied missing data types in the data to be consistent
# (all missing values should be displayed as "NaN") and save the new data
# as a JSON file.

#%%
flights.isnull().sum()

#%%
flights.describe()

#%%
flights_new = flights.replace