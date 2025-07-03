import pandas as pd
#Pandas is a Python library for data analysis, cleaning, manipulation, and exploration.
''' It gives you:

DataFrames (like tables)
Series (like columns)
Superpowers to work with CSV, Excel, JSON, etc.

It provides powerful data structures:

Series → 1D (like a column)

DataFrame → 2D (like a table/spreadsheet)



'''
data ={
    'Name': ['Krrish','varun','jaimin'],
    'Age' : [20,21,19],
    'city':['Ahemedabad','Delhi','Mumbai']
    }


df= pd.DataFrame(data)
print(df)


# let's create a series 

import pandas as pd

data1=[22,34,23,78.98]
srd=pd.Series(data1)
print(srd)


# let's move to the csv files 

import pandas as pd
df1= pd.read_csv(r"C:\Users\Admin\Desktop\python krrishhh\AI-ML\learningdatascience\first.csv")

print(df1)


import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\Admin\Desktop\python krrishhh\AI-ML\learningdatascience\first.csv")

# Explore the data
# print("📌 First 5 rows:\n", df.head(), "\n")
# print("📌 Last 5 rows:\n", df.tail(), "\n")
# print("📌 Shape (rows, columns):", df.shape, "\n")
# print("📌 Column names:", df.columns.tolist(), "\n")
# print("📌 Info:")
# df.info()
# print("\n📌 Summary statistics (only numeric columns):\n", df.describe())

print(df.head())
print(df.tail())
print("rows,collumns:",df.shape)
df.info()
print(df.columns.to_list())
print(df.describe())


#Selecting and Filtering Data
"""
🧠 What is Indexing and Slicing?
Think of a DataFrame like an Excel table.

Indexing = Selecting specific rows/columns.

Slicing = Cutting out a range (like row 1 to 5)."""


import pandas as pd 

dataofindexing = {
     "Name" :["krish","vraj","varun","kylo","anakin"]
     ,"Age" : [22,34,23,78.98,45]
     ,"city" :["ahemedabad","mumbai","delhi","pune","chennai"]
}
dfi= pd.DataFrame(dataofindexing)
print(dfi)

#🔍 1. Select a Single Column

print("here")

print(dfi['Age'])


dfi = pd.DataFrame(dataofindexing)
print("now")

print(dfi[dfi['Age']>30],"\n")                         # dfi[ condition goes here ]

# 🔍 1. Filter: People older than 30
# Shows rows where Age > 30
print("👉 People older than 30:\n", dfi[dfi['Age'] > 30], "\n")

# 🔍 2. Filter: People from Mumbai
# Matches exact string in 'city' column
print("👉 People from Mumbai:\n", dfi[dfi['city'] == 'mumbai'], "\n")

# 🔍 3. Filter: Age between 25 and 50
# Combines two conditions using '&' (and)
print("👉 People with age between 25 and 50:\n", dfi[(dfi['Age'] >= 25) & (dfi['Age'] <= 50)], "\n")

# 🔍 4. Filter: City is either Pune or Delhi
# Uses .isin() to check if value is in the list
print("👉 People from Pune or Delhi:\n", dfi[dfi['city'].isin(['pune', 'delhi'])], "\n")


#🔍 3. Selecting Rows and Columns: 
# .iloc vs .loc

print(df.iloc[0])            # Entire first row
print(df.iloc[1:4])          # Rows 1 to 3
print(df.iloc[:, 1])         # All 'Age' column values
print(df.iloc[2, 0])         # 'Varun' (row 2, column 0)

# loc
print(df.loc[0])                       # Entire first row (label 0)
print(df.loc[1:3])                     # Rows 1 to 3 (inclusive)
print(df.loc[:, 'Name'])              # All names
print(df.loc[2, ['Name', 'Age']])    # 'Varun' and 'Delhi'


## range(1, 5)  # This is NOT inclusive of 5
## Output: 1, 2, 3, 4 ❌ 5 not included
