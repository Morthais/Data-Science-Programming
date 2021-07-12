'''
GRAND QUESTION 2
If you talked to someone named Brittany on the phone, 
what is your guess of his or her age? What ages would 
you not guess?

Based on the given data, I would expect Brittany to have been
born in the year 1990, but not before 1982 or after 1998.

That would mean I guess Brittany to be about 31 years old, but
I would not guess Brittany to be older than 39 or younger than
23 years old since the occurence of the name Brittany is lower 
before 1982 and after 1998 than at the names' peak in 1990.

Any guess between 23 and 39 years old would be acceptable, but
31 years is the most likely answer.

Fun fact: Brittany Spears debuted in the late-1990's, so we can
rule out that the name Brittany became popular because of her.
'''
#%%
# load packages pandas and altair
import pandas as pd
import altair as alt

#%%
# load names data from url
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
namesDataFrame = pd.read_csv(url)

#%%
# build (query) DataFrame for Brittany from the namesDataFrame
name = namesDataFrame.query('name == "Brittany"')

#%%
# build chart from 'name' DataFrame
name_chart = (alt.Chart(name)
    .encode(
        x = 'year',
        y = 'Total'
    )
    .mark_line()
)

#%%
# build charts of peak year and low years from Brittany 'name' DataFrame
# horizontal line created with .mark_rule() and name.query("year == 1990")
# this narrows the overlay chart to contain only data from the peak year
overlay_peakYear = (alt.Chart(name.query("year == 1990"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
            #color = 'name'
        )
    # attributes go here
    .mark_rule(color = 'red')
)

overlay_lowYears = (alt.Chart(name.query("year == 1982 | year == 1998"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
            #color = 'name'
        )
    # attributes go here
    .mark_rule(color = 'red')
)

#%%
# layer, configure, and print name and overlay chart as one chart using alt.layer()
# answers ages I would guess
finalChart_peak = (alt.layer(name_chart, overlay_peakYear)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
    # add a title and subtitle to the chart
    .properties(
        title = {
            "text": "Births of Name 'Brittany' Throughout History",
            "subtitle": "The Peak for 'Brittany' was in 1990"
        }
    )
)

finalChart_peak

#%%
# layer, configure, and print name and overlay chart as one chart using alt.layer()
# answers ages I would not guess
finalChart_low = (alt.layer(name_chart, overlay_lowYears)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
    # add a title and subtitle to the chart
    .properties(
        title = {
            "text": "Births of Name 'Brittany' Throughout History",
            "subtitle": "The Lows for 'Brittany' are before 1982 and after 1998"
        }
    )
)

finalChart_low

#%%
# save the peak chart (would guess)
finalChart_peak.save("Images/peakBrittanyChart.png")

#%%
# save the low chart (would not guess)
finalChart_low.save("Images/lowBrittanyChart.png")
