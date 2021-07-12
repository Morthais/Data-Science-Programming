#%%
# import package
import datadotworld as dw

#%%
# Query byuidss/cse-250-baseball-database to Select all columns from Pitching
# Join shared columns from Pitching and Salaries tables,
pitch = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT DISTINCT Salaries.salary,
           Pitching.playerID,
           Pitching.yearID,
           Pitching.teamID,
           Pitching.lgID
    FROM Salaries
        JOIN Pitching ON Pitching.playerID = Salaries.playerID
    WHERE Pitching.yearID = 1986
    ORDER BY salary DESC
    LIMIT 306
    '''
).dataframe

print(pitch)

#%%
# Query the number of Pitchers (count of playerID) the Washington Nationals used in each year
# Order by yearID
num_of_pitchers_each_year_WN = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT COUNT(PitchingPost.playerID) AS num_pitchers,
           PitchingPost.yearID AS year,
           PitchingPost.teamID AS team
    FROM PitchingPost
    GROUP BY PitchingPost.yearID
    ORDER BY PitchingPost.yearID
    '''
).dataframe

print(num_of_pitchers_each_year_WN)

# %%
# Methods and Calculations
batting_avg_A = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT DISTINCT Batting.playerID,
        Batting.yearID,
        Batting.H,
        Batting.AB,
        (Batting.H / Batting.AB) AS BattingAVG
    FROM Batting
    LIMIT 2
    '''
).dataframe

# %%
batting_avg_A
# %%
