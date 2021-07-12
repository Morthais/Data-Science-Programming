'''
GRAND QUESTION 1
How does your name at your birth year compare to its use historically?

I was born in the year 1998, which was the peak year for babies given
the name 'Jacob' at their birth. My parents were totally unoriginal,
but I am grateful for the name I've been given.
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
# list the data types
namesDataFrame.dtypes

#%%
# show the original raw data
namesDataFrame

#%%
# build (query) DataFrame for Jacob from the namesDataFrame
name = namesDataFrame.query('name == "Felisha"')
name

#%%
# Calculate and print total names Oliver occurs in UT
Total = name['UT'].sum()
print(Total)

#%%
# build chart from 'name' DataFrame
name_chart = (alt.Chart(name)
    .encode(
        x = 'UT',
        y = 'Total'
    )
    .mark_bar()

    # add a title and subtitle to the chart
    # TO DO: move to layer method to see if it still works
    .properties(
        title = {
            "text": "Births of Name 'Jacob' Throughout History",
            "subtitle": "I was born in the year 1998"
        }
    )
)

name_chart
#%%
# build chart of peak year from 'name' DataFrame
# horizontal line created with .mark_rule() and name.query("year == 1998")
# this narrows the overlay chart to contain only data from the peak year
overlay = (alt.Chart(name.query("year == 1998"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total'
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
            #color = 'name'
        )
    # attributes go here
    .mark_rule(color = 'red')
)
#%%
# layer, configure, and print name and overlay chart as one chart using alt.layer()
final_chart = (alt.layer(name_chart, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart 

#%%
# save the chart
final_chart.save("Images/birthYearChart.png")
