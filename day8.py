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

# ── Sample DataFrames ────────────────────────────────────────────────────────
df_left = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Name' : ['Alice', 'Bob', 'Charlie']
})

df_right = pd.DataFrame({
    'EmpID': [2, 3, 4],
    'Department': ['HR', 'IT', 'Finance']
})

print("LEFT (df_left):")
print(df_left, "\n")
print("RIGHT (df_right):")
print(df_right, "\n")

# ── 1) INNER JOIN ────────────────────────────────────────────────────────────
inner_join = pd.merge(df_left, df_right, on='EmpID', how='inner')
print("▶ INNER JOIN (only matching EmpID rows)\n", inner_join, "\n")

# ── 2) LEFT JOIN ─────────────────────────────────────────────────────────────
left_join = pd.merge(df_left, df_right, on='EmpID', how='left')
print("▶ LEFT JOIN (all rows from df_left)\n", left_join, "\n")

# ── 3) RIGHT JOIN ────────────────────────────────────────────────────────────
right_join = pd.merge(df_left, df_right, on='EmpID', how='right')
print("▶ RIGHT JOIN (all rows from df_right)\n", right_join, "\n")

# ── 4) OUTER JOIN ────────────────────────────────────────────────────────────
outer_join = pd.merge(df_left, df_right, on='EmpID', how='outer')
print("▶ OUTER JOIN (union of both tables)\n", outer_join)


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

"""
LEFT (df_left):
   EmpID     Name
0      1    Alice
1      2      Bob
2      3  Charlie 

RIGHT (df_right):
   EmpID Department
0      2         HR
1      3         IT
2      4     Finance 

▶ INNER JOIN (only matching EmpID rows)
   EmpID     Name Department
0      2      Bob         HR
1      3  Charlie         IT 

▶ LEFT JOIN (all rows from df_left)
   EmpID     Name Department
0      1    Alice        NaN
1      2      Bob         HR
2      3  Charlie         IT 

▶ RIGHT JOIN (all rows from df_right)
   EmpID     Name Department
0      2      Bob         HR
1      3  Charlie         IT
2      4      NaN     Finance 

▶ OUTER JOIN (union of both tables)
   EmpID     Name Department
0      1    Alice        NaN
1      2      Bob         HR
2      3  Charlie         IT
3      4      NaN     Finance


"""