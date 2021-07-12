#%%
# import packages
import datadotworld as dw

# GRAND QUESTION 1

#%%
# Query byuidss/cse-250-baseball-database CollegePlaying and Salaries tables as one dataframe
# Include CollegePlaying.playerID, CollegePlaying.schoolID, Salaries.salary, Salaries.yearID, Salaries.teamID
# Only include baseball players who attended BYU-Idaho
# Order by salary (highest to lowest)
# TODO: Include the table in your Markdown report

baseball_byuIdaho = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT DISTINCT CollegePlaying.playerID,
        CollegePlaying.schoolID,
        Salaries.salary,
        Salaries.yearID,
        Salaries.teamID
    FROM CollegePlaying
        JOIN Salaries 
            ON CollegePlaying.playerID = Salaries.playerID
    WHERE CollegePlaying.schoolID = "idbyuid"
    ORDER BY Salaries.salary DESC
    '''
).dataframe

print(baseball_byuIdaho.to_markdown())

# %%
