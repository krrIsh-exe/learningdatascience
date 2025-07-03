import pandas as pd

dataframe ={

    "Name" : ["krish","kylo","vraj","varun","jaimin"],
   "Age" : [23,45,22,21,33],
   "City" :["Ahemedabad","delhi","bengluru","chennai","lakhnau"]

}

df =pd.DataFrame(dataframe)
print(df)

##START###

df[df['Age'] > 30]                             # Age greater than 30
df[(df['Age'] > 30) & (df['City'] == 'Delhi')] # Age > 30 AND city is Delhi
df[(df['City'] == 'Mumbai') | (df['Age'] < 25)] # OR condition


print(df[ df ['City'].isin(['delhi','Ahemedabad'])])


#🔹 7. Using .query() (SQL-style filtering)

print(df.query('Age > 30 and City == "Delhi"'))


#                            📊 Topic 3: groupby() — Grouping and Aggregation 


import pandas as pd 

data = {
    'Department' :['IT', 'HR', 'IT', 'HR', 'Sales', 'Sales', 'IT'],
    'employee' : ['A','b','c','d','e','f','g'],
    'Salary' :[50000, 40000, 55000, 42000, 30000, 35000, 60000]
  }

df1 = pd.DataFrame(data)
print(data)

#groupby
#🔹 What groupby() Does:
# It groups rows that have the same value in the specified column — just like making teams based on department, city, name, etc.

print(df1.groupby('Department')['Salary'].sum())
        
      # 👉 Group by department and apply multiple aggregations
result = df1.groupby('Department').agg(
    Total_Salary=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Employee_Count=('Salary', 'count'),
    Max_Salary=('Salary', 'max')
)

print(result)