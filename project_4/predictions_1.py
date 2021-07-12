#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#%%
# import data
alt.data_transformers.disable_max_rows()

dwellings_denver_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'
dwellings_ml_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv'
dwellings_neighborhoods_ml_url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv'

dwellings_denver = pd.read_csv(dwellings_denver_url)
dwellings_ml = pd.read_csv(dwellings_ml_url)
dwellings_neighborhoods_ml = pd.read_csv(dwellings_neighborhoods_ml_url)

#%%
# what are we looking at?
dwellings_ml.columns

# GRAND QUESTION 1
# Create 2-3 charts that evaluate potential relationships between the home variables and before1980.

# Name the features (we only want unique data... no redundant or irrelevant features)
# Don't choose too many... could reduce the accuracy of the predictions.
# Only choose features you understand yourself.
# 'yrbuilt', 'sprice', 'stories', 'nocars', 'livearea','numbrdm','numbaths',

# Name the targets
# 'before1980'

#%%
# create a table for the charts
dwellings_table = (dwellings_ml
    .groupby('yrbuilt')
        .agg(
            sprice_avg = ('sprice', np.average),
            stories_avg = ('stories', np.average),
            nocars_avg = ('nocars', np.average),
            livearea_avg = ('livearea', np.average),
            numbdrm_avg = ('numbdrm', np.average),
            numbaths_avg = ('numbaths', np.average)
        )
        .filter(
            ['yrbuilt', 'sprice_avg', 'stories_avg', 'nocars_avg', 'livearea_avg', 'numbdrm_avg', 'numbaths_avg']
        )
        .reset_index()
    )

dwellings_table

#%%
# create an overlay chart to mark 1980
overlay = (alt.Chart(dwellings_table.query("yrbuilt == 1980"))
    .encode(
        # variables go here
            x = 'yrbuilt'
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
            #color = 'name'
        )
    # attributes go here
    .mark_rule(color = 'red')
)

#%%
chart1 = alt.Chart(dwellings_table).mark_area().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('sprice_avg', axis=alt.Axis(title="Average Selling Price"))
).properties(
    title = {
        "text":"Average Selling Price of a House each Year",
    }
)

# overlay the charts to create a better chart
final_chart1 = (alt.layer(chart1, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart1.save("Images/AvgSellingPriceEachYear.png")

#%%
chart2 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('stories_avg', axis=alt.Axis(title="Average Number of Stories"))
).properties(
    title = {
        "text":"Average Number of Stories in a House each Year",
    }
)

# overlay the charts to create a better chart
final_chart2 = (alt.layer(chart2, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart2.save("Images/AvgNumberOfStoriesEachYear.png")

#%%
chart3 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('nocars_avg', axis=alt.Axis(title="Average Number of Cars"))
).properties(
    title = {
        "text":"Average Number of Cars Fitting in a House Garage each Year",
    }
)

# overlay the charts to create a better chart
final_chart3 = (alt.layer(chart3, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart3.save("Images/AvgNumberOfCarsEachYear.png")

#%%
chart4 = alt.Chart(dwellings_table).mark_area().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('livearea_avg', axis=alt.Axis(title="Average Living Area (in sqft)"))
).properties(
    title = {
        "text":"Average Living Area in a House each Year",
    }
)

# overlay the charts to create a better chart
final_chart4 = (alt.layer(chart4, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart4.save("Images/AvgLivingAreaEachYear.png")

#%%
chart5 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('numbdrm_avg', axis=alt.Axis(title="Average Number of Bedrooms"))
).properties(
    title = {
        "text":"Average Number of Bedrooms in a House each Year",
    }
)

# overlay the charts to create a better chart
final_chart5 = (alt.layer(chart5, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart5.save("Images/AvgNumberOfBedroomsEachYear.png")

#%%
chart6 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('numbaths_avg', axis=alt.Axis(title="Average Number of Bathrooms"))
).properties(
    title = {
        "text":"Average Number of Bathrooms in a House each Year",
    }
)

# overlay the charts to create a better chart
final_chart6 = (alt.layer(chart6, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)

final_chart6.save("Images/AvgNumberOfBathroomsEachYear.png")

# %%
