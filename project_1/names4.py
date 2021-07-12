'''
GRAND QUESTION 4
Think of a unique name from a famous movie. Plot the usage of 
that name and see how changes line up with the movie release.

The name I chose was Harrison, after the actor Harrison Ford.
I plotted the usage of his first name every time a Star Wars
Episode is released. According to the Data, there seem to be
both upward and downward trends of the birth name Harrison
when a Star Wars Episode is released. This makes sense with
the middle three, since those Episodes did not include the 
actor Harrison Ford. However, every episode which includes 
Harrison Ford is associated with an upward trend in the usage
of the birth name Harrison. Are the two connected? Maybe!
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
# build (query) DataFrame for Harrison from the namesDataFrame
name = namesDataFrame.query('name == "Harrison"')

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
# build overlay charts of Star Wars Episode release years
# horizontal line created with .mark_rule() and name.query("year == 1990")
# this narrows the overlay chart to contain only data from the release year
release_episodeIV = (alt.Chart(name.query("year == 1977"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

release_episodeV = (alt.Chart(name.query("year == 1980"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

release_episodeVI = (alt.Chart(name.query("year == 1983"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

release_episodeI = (alt.Chart(name.query("year == 1999"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

release_episodeII = (alt.Chart(name.query("year == 2002"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

release_episodeIII = (alt.Chart(name.query("year == 2005"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

release_episodeVII = (alt.Chart(name.query("year == 2015"))
    .encode(
        # variables go here
            x = 'year',
            y = 'Total',
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
        )
    # attributes go here
    .mark_rule(color = 'red')
)

#%%
# layer, configure, and print name and overlay chart as one chart using alt.layer()
# answers ages I would guess
finalChart = (alt.layer(name_chart, release_episodeI, release_episodeII, release_episodeIII, release_episodeIV, release_episodeV, release_episodeVI, release_episodeVII)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
    # add a title and subtitle to the chart
    .properties(
        title = {
            "text": "Births of Name 'Harrison' When Star Wars Movies Debuted",
            "subtitle": "Release years marked for Star Wars Episode I to Episode VII"
        }
    )
)

finalChart

#%%
# save the peak chart (would guess)
finalChart.save("Images/starWarsChart.png")

# %%
