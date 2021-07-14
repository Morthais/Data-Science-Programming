# %%
# load packages
import pandas as pd
import altair as alt

# data url
starwars_file_path = "../../data/raw_data/StarWars.csv"

# load data and columns
starwars = pd.read_csv(starwars_file_path, encoding = "ISO-8859-1", skiprows = 2, header = None)
starwars_cols = pd.read_csv(starwars_file_path, encoding = "ISO-8859-1", nrows = 2, header = None)

#%%
# clean up the column names
column_names_1 = starwars_cols.iloc[0,:]
column_names_1 = (column_names_1
                  .replace("Have you seen any of the 6 films in the Star Wars franchise?", "seen_any_films?")
                     .replace("Which of the following Star Wars films have you seen? Please select all that apply.", "seen_which_films?")
                     .replace("Which character shot first?", "who_shot_first?")
                     .str.replace(" ", "_")
                     .str.replace("[(|)\?]", "")
                     .str.replace("æ", "")
                     .str.lower()
                     .ffill())
print(column_names_1)

column_names_2 = starwars_cols.iloc[1,:]
column_names_2 = (column_names_2
                   .replace("Response", "")
                   .str.replace("Star Wars: Episode ", "")
                   .str.replace(" ", "_")
                   .fillna("")
                   .str.lower())
print(column_names_2)

full_column_names = column_names_1 + column_names_2
starwars.columns = full_column_names

#starwars = starwars.query('have_seen_any == "Yes"')

starwars.head()

# %%
#--------- Calculate some statistics ----------
total_people = starwars.respondentid.nunique()
total_people

#%%
table1 = starwars.have_seen_any.value_counts().reset_index()
table1['percent'] = table1.have_seen_any / total_people
table1


# %%
table1 = starwars.have_seen_any.value_counts(normalize = True).reset_index()
table1

# %%
table1 = starwars.value_counts(subset = ['have_seen_any','gender']).reset_index()
table1

# %%
#--------- Make some charts! ----------
starwars.shot_first.value_counts()

#%%
starwars.shot_first.value_counts(normalize=True).reset_index()

#%%
(starwars.shot_first
 .fillna("Missing")
 .value_counts(normalize=True)
 .reset_index())



# %%
# Another chart:
# Getting percentage of respondents that have seen each movie

# Method 1 - The "R way" using melt()
bob = starwars.melt(
    id_vars = ['respondentid'],
    value_vars = ['seen_film_i__the_phantom_menace',
                  'seen_film_ii__attack_of_the_clones', 
                  'seen_film_iii__revenge_of_the_sith',
                  'seen_film_iv__a_new_hope', 
                  'seen_film_v_the_empire_strikes_back',
                  'seen_film_vi_return_of_the_jedi']
)

bob.sort_values('respondentid')

#%%
bob.value.value_counts(normalize=True).reset_index()

# %%
print(bob.respondentid.nunique())
print(bob.dropna(subset=['value']).respondentid.nunique())

#%%
num_people = bob.dropna(subset=['value']).respondentid.nunique()
table2 = bob.value.value_counts().reset_index()
table2['percent'] = table2.value / num_people
table2


# %%
# Method 2 - A more direct approach 

# this is not quite right
watched = starwars.filter(regex='seen_film')
print(len(watched))

watched_percent = round(watched.notnull().sum() / len(watched), 2).reset_index(name='percent')
watched_percent

# %%
# this is not quite right
watched = starwars.query('have_seen_any == "Yes"').filter(regex='seen_film')
print(len(watched))

watched_percent = round(watched.notnull().sum() / len(watched), 2).reset_index(name='percent')
watched_percent

# %%
# better!!
watched = starwars.filter(regex='seen_film').dropna(how = "all")
print(len(watched))

#%%
watched_percent = round(watched.notnull().sum() / len(watched), 2).reset_index(name='percent')
watched_percent

# %%
