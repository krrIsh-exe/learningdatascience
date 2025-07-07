# Merging And joining Dataframes
# 💡 Imagine This Scenario
# 🗂️ Sheet 1: Employee Names (df1)
# EmpID	Name
# 1	Alice
# 2	Bob
# 3	Charlie

# 🗂️ Sheet 2: Employee Departments (df2)
# EmpID	Department
# 2	HR
# 3	IT
# 4	Finance

# 🧠 Goal:
# You want to combine both sheets to see:

# “Which employee is in which department?”

# 🛠 Code:
# python
# Copy
# Edit
import pandas as pd

df1 = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'EmpID': [2, 3, 4],
    'Department': ['HR', 'IT', 'Finance']
})

# Merge on EmpID (like a common ID)
merged_df = pd.merge(df1, df2, on='EmpID', how='inner')
print(merged_df)

# ✅ Output:
# nginx
# Copy
# Edit
#    EmpID    Name Department
# 0      2     Bob         HR
# 1      3  Charlie         IT
# 👉 It joined the rows where EmpID matches.

# 📊 Different Types of Join:
# 🔁 Try changing how='inner' to:
# Join Type	What it does
# inner	Only shows matching EmpIDs in both tables
# left	Shows all from df1, fills blanks if needed
# right	Shows all from df2, fills blanks if needed
# outer	Shows all from both, fills missing with NaN