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
