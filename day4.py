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