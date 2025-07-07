###            📊 Sorting & Ranking in Pandas


import pandas as pd 

# Here we created dataframe
data = {
'Department': ['IT', 'HR', 'IT', 'HR', 'Sales', 'Sales', 'IT'],
'employee' :['A','b','c','d','e','f','g'],
'Salary':[50000, 40000, 55000, 42000, 30000, 35000, 60000],
'Age':[22,34,32,22,44,32,21]
}

df =pd.DataFrame(data)
print(df)

# now we will perform sorting operations on it

print(df.sort_values('Age'))   #  it will sort age in ascending order lowest to highest

# For decending order we will do like this 
print(df.sort_values('Age',ascending=False))

print(df.sort_index(ascending=False)) # decending orderindexing


print(df.sort_values(['Department', 'Salary']))   #➡️ First by 'Department', then by 'Salary' within each department.

df['Salary_Rank'] = df['Salary'].rank(ascending=False)  #➡️ Higher salary gets rank 1.
print(df)

