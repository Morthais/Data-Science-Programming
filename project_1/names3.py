'''
GRAND QUESTION 3
Mary, Martha, Peter, and Paul are all Christian names. From 1920 
to 2000, compare the name usage of each of the four names.
'''
### TO DO: Add a legend to the final chart.

#%%
# load packages pandas and altair
import pandas as pd
import altair as alt

#%%
# load names data from url
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
namesDataFrame = pd.read_csv(url)

#%%
# read data types
namesDataFrame.dtypes

#%%
# build (query) DataFrame for christianNames from the namesDataFrame
christianNames = namesDataFrame.query('name == "Mary" | name == "Martha" | name == "Peter" | name == "Paul"')

#%%
# build (query) christianNames for Mary, Martha, Peter, and Paul
nameMary = christianNames.query('name == "Mary"')
nameMartha = christianNames.query('name == "Martha"')
namePeter = christianNames.query('name == "Peter"')
namePaul = christianNames.query('name == "Paul"')

#%%
# create Mary overlay chart
overlay_Mary = (alt.Chart(nameMary)
    .encode(
        # variables go here
        x = 'year',
        y = 'Total',
        # variables for .mark_point()
        #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        color = 'name'
    )
    # attributes go here
    .mark_line()
)

#%%
# create Martha overlay chart
overlay_Martha = (alt.Chart(nameMartha)
    .encode(
        # variables go here
        x = 'year',
        y = 'Total',
        # variables for .mark_point()
        #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        color = 'name'
    )
    # attributes go here
    .mark_line()
)

#%%
# create Peter overlay chart
overlay_Peter = (alt.Chart(namePeter)
    .encode(
        # variables go here
        x = 'year',
        y = 'Total',
        # variables for .mark_point()
        #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        color = 'name'
    )
    # attributes go here
    .mark_line()
)

#%%
# create Paul overlay chart
overlay_Paul = (alt.Chart(namePaul)
    .encode(
        # variables go here
        x = 'year',
        y = 'Total',
        # variables for .mark_point()
        #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        color = 'name'
    )
    # attributes go here
    .mark_line()
)

#%%
# layer, configure, and print all charts as one chart using alt.layer()
# answers ages I would guess
finalChart = (alt.layer(overlay_Mary, overlay_Martha, overlay_Peter, overlay_Paul)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
    # give the final chart a title
    .properties(
        title = {
            "text": "Births of Christian Names from 1920 to 2000",
            "subtitle": "Compares Names Mary, Martha, Peter, and Paul"
        }
    )
)

finalChart

#%%
# save the christian names chart
finalChart.save("Images/christianNamesChart.png")

# %%
