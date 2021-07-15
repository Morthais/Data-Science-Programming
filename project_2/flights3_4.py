#%%
# import packages
import altair as alt
import pandas as pd
import numpy as np

#%%
# from json url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)

# GRAND QUESTION 3
# The Total Number of Flights Delayed by Weather: 1,068,267 flights delayed

#%%
# What data are we dealing with?
flights.columns

#%%
# create a weather delays dataframe
weather_delays = (flights
    .assign(
        # select all missing values in num_of_delays_late_aircraft and replace with the mean
        severe = lambda x: x.num_of_delays_weather.replace(-999, x.num_of_delays_weather.mean()),
        # calculate 30% of late-arriving aircraft to find mild weather delays
        mild_late = lambda x: x.num_of_delays_late_aircraft * .30,
        # calculate 40% of nas flights from Apr - Aug and 65% otherwise to find mild weather delays
        mild_nas = lambda x: np.where(
            x.month.isin(["April", "May", "June", "July", "August"]),
            x.num_of_delays_nas * .40,
            x.num_of_delays_nas * .65),
        # calculate today weather delays for each observation (row)
        total_weather = lambda x: x.severe + x.mild_late + x.mild_nas,
        # calculate total late aircraft to help calculate which proportion (percent) of late aircraft are due to weather
        total_late = lambda x: x.num_of_delays_weather + x.num_of_delays_late_aircraft + x.num_of_delays_nas,
        # calculate which proportion (percent) of late aircraft are due to weather
        percent_weather = lambda x: x.total_weather / x.total_late,
        # calculate the actual number we're looking for... total number of flights delayed by weather
        total_weather_sum = lambda x: sum(x.severe) + sum(x.mild_late) + sum(x.mild_nas),
    )
    .filter(
        ['airport_code', 'month', 'severe','mild_late','mild_nas', 'total_weather', 'total_late', 'percent_weather', 'total_weather_sum']
    )
)

#%%
# convert table to markdown
print(weather_delays.head(5).to_markdown())

#%%
# What is the total number of flights delayed by any weather?
print(weather_delays['total_weather_sum']) # 1068267.05

# GRAND QUESTION 4
# This chart shows that the Atlanta airport has the worst ratio of delays caused by weather, meaning we can
# expect the majority of delays have to do with weather for flights involving the Atlanta airport.

#%%
# create a barplot showing the proportion of all flights delayed by weather at each airport
weather_chart = alt.Chart(weather_delays).mark_bar().encode(
    x = alt.X('airport_code', axis=alt.Axis(title='Airport')),
    y = alt.Y('percent_weather', axis=alt.Axis(format="%", title='Proportion of Flights Delayed by Weather'))
).properties(
    title = {
        "text":"Proportion of Flights Delayed by Airport",
        "subtitle":"The most weather delays take place with the Atlanta airport."
    }
)

weather_chart.save("Images/weather_chart.png")

# %%
