# 📚 Topics i will Learn in Data Preprocessing:
# Step	Topic	Why It's Important
# 1	Handling Missing Values (fillna, dropna)	Clean messy data (you already did this in Pandas!)
# 2	Label Encoding & One-Hot Encoding	Convert categorical text to numbers for ML models
# 3	Feature Scaling	Make sure features are in the same range (e.g., age vs salary)
# 4	Train-Test Split	Split your data to train models properly
# 5	Outlier Removal (optional)	Eliminate extreme, incorrect values
# 6	Feature Selection (optional)	Keep only the most useful data columns


# ✅ When to Use crosstab() vs pivot_table():

# Feature	          crosstab()	                                     pivot_table()

# Used For	          Counting combos (frequencies)	                     Aggregating values (mean/sum)
# Aggregation Type	  Always counts	                                     Can do sum, mean, etc.
# Simplicity	      Simpler	                                         More customizable
# Output	          Summary table	                                     Summary table

# In data analysis, pivot means:
# To turn your data so you can view it from a different angle or perspective.

import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Sales', 'Sales', 'IT'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'Salary': [50000, 40000, 55000, 42000, 30000, 35000, 60000]
}

df = pd.DataFrame(data)
print(df)

pivot = df.pivot_table(
    index='Department',        # Rows
    columns='Gender',          # Columns
    values='Salary',           # What to summarize
    aggfunc='mean'             # How to summarize (mean = average)
)
print(pivot)

# Feature	Purpose
# pivot_table()	Reshape and summarize data
# index	What becomes the rows
# columns	What becomes the sub-columns
# values	What to calculate (e.g., salary, marks)
# aggfunc	Aggregation method (e.g., mean, sum)
# margins=True	Add total row/column
