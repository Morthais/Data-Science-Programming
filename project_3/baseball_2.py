#%%
# import packages
import datadotworld as dw

# GRAND QUESTION 2

#%%
# PART A
# Batting Average == player's hits (H) / player's at-bats (AB)
# Query Batting.playerID, Batting.yearID, and batting average (Batting.H / Batting.AB)
# Only include players with AT LEAST 1 BAT
# Order by batting average (highest to lowest) and only show top 5 results
batting_avg_A = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT DISTINCT Batting.playerID,
        Batting.yearID,
        Batting.H,
        Batting.AB,
        (Batting.H / Batting.AB) AS BattingAVG
    FROM Batting
    WHERE Batting.AB >= 1
    ORDER BY BattingAVG DESC
    LIMIT 5
    '''
).dataframe

print(batting_avg_A.to_markdown())

#%%
# PART B
# Query Batting.playerID, Batting.yearID, and batting average (Batting.H / Batting.AB)
# Only include players with AT LEAST 10 BATS
# Order by batting average (highest to lowest) and only show top 5 results
batting_avg_B = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT DISTINCT Batting.playerID,
        Batting.yearID,
        Batting.H,
        Batting.AB,
        (Batting.H / Batting.AB) AS BattingAVG
    FROM Batting
    WHERE Batting.AB >= 10
    ORDER BY BattingAVG DESC
    LIMIT 5
    '''
).dataframe

print(batting_avg_B.to_markdown())

# PART C
# %%
# Query Batting.playerID, Batting.yearID, and batting average (Batting.H / Batting.AB)
# Calculate the sum of BattingAVG over playerID career
# Only include players with AT LEAST 100 BATS
# Order by batting average (highest to lowest) and only show top 5 results
batting_avg_C = dw.query('byuidss/cse-250-baseball-database',
    '''
    SELECT DISTINCT Batting.playerID,
        Batting.H,
        Batting.AB,
        (Batting.H / Batting.AB) AS BattingAVG
    FROM Batting
    WHERE Batting.AB >= 100
    GROUP BY Batting.playerID
    ORDER BY BattingAVG DESC
    LIMIT 5
    '''
).dataframe

print(batting_avg_C.to_markdown())

# %%
