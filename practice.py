import pandas as pd

df = pd.read_csv('disney_plus_titles.csv')
print(df)

#see First 5 rows 

print (df.head())

# Let’s pick just a few clean columns to reshape, like:
df_small =df[['title','type','release_year', 'rating']]
print(df_small.head())

#melt
melted= pd.melt(df_small,
    id_vars=['title', 'type'],       # Keep title & type fixed
    var_name='Feature',              # Name of new column for melted column names
    value_name='Value'               # Name of new column for melted values
)
print(melted.head(10))