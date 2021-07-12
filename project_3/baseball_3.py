#%%
# import packages
import datadotworld as dw
import altair as alt

# GRAND QUESTION 3

#%%
# Pick two baseball teams (Atlanta Braves (teamID = ATL), Detroit Tigers (teamID = DET))
# compare them however you choose (number of wins)
# Query the data needed to compare these teams 
# (Teams.teamID, Teams.W)
compare_ATL_DET = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT Teams.teamID,
        Teams.W AS Wins,
        Teams.L AS Losses,
        (Teams.W / Teams.L) AS Win_Loss_Ratio
    FROM Teams
    WHERE Teams.teamID = 'ATL'
        OR Teams.teamID = 'DET'
    GROUP BY Teams.teamID
    '''
).dataframe

print(compare_ATL_DET.to_markdown())

#%%
# make an Altair graph to visualize the comparison (x = Team, y = ??? (comparison))
# use python to wrangle the data if needed

chart = alt.Chart(compare_ATL_DET).encode(
    x = alt.X('Win_Loss_Ratio', axis=alt.Axis(title='Team Performance')),
    y = alt.Y('teamID', axis=alt.Axis(title="Teams"))
).mark_bar().properties(
    title = {
        "text":"Which team performs better: Atlanta Braves or Detroit Tigers?",
        "subtitle":"Decided by a wins/losses ratio. (higher is better)"
    }
)

chart.save("Images/compare_ATL_DET.png")
# %%
