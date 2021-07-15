#%%
# import packages
import altair as alt
from altair.vegalite.v4.schema.channels import Row
import pandas as pd
import numpy as np

#%%
# from json url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)

# GRAND QUESTION 2
# The best month to fly to avoid delays of any length is November. I chose this month based on the chart I created,
# which shows the total number of delays each month. If the total count of delays in any given month is lower than
# any other month, then the chances of a delay happening in that month is also less than any other month. Therefore, 
# November is the best month to fly in order to avoid delays of any length because the total count of delays is lowest in November.

#%%
# What data are we dealing with?
flights.columns

# %%
# Create a new data frame containing all data pertaining to delays, 
# but group by month instead of by airport.
# TODO: Order by Month
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

best_months.sort_values(by="month", ascending=False)

# %%
# include one chart to help support your answer
best_month_chart = alt.Chart(best_months).mark_bar().encode(
    x = alt.X('month', axis=alt.Axis(title='Month')),
    y = alt.Y('delays_total', axis=alt.Axis(title='Total Count of Delays'))
).properties(
    title = {
        "text":"Total Number of Delays Each Month",
        "subtitle":"The highest is July and the lowest is November"
    }
)

best_month_chart

#%%
# save the chart
best_month_chart.save("Images/best_month_chart.png")

# %%
