"""📌 Why Handle Missing Data?
Real-world datasets are messy — some values are often missing (NaN = Not a Number).

We need to:

Detect missing values

Decide whether to remove or fill them

Handling missing data is not just about cleaning;
it's about preserving the integrity and usefulness of your dataset. 
By thoughtfully detecting missing values and strategically deciding whether to remove or impute them,
you ensure that your statistical analyses are robust and your machine learning models are accurate and reliable.
Ignoring missing data is a recipe for misleading results and poor decision-making.
NaN is a ubiquitous placeholder in data science for values that are absent, unknown, or mathematically undefined.
Understanding its behavior is fundamental to cleaning and preparing data effectively.


Even though np.nan means "Not a Number", Pandas still uses it as a universal marker for missing data, including:

🧮 Numbers (int, float)

🔤 Strings (text)

🗓️ Dates

💯 Booleans
"""

import pandas as pd
import numpy as np

data = {
    'Name': ['Krish', 'Kylo', 'Varun', 'Meera', 'Neo'],
    'Age': [23, np.nan, 21, 24, np.nan],
    'City': ['Ahmedabad', 'Delhi', np.nan, 'Mumbai', 'Chennai']
}


df = pd.DataFrame(data)
print(df)


df.isnull()
# this is used to function to find missing values
print(df.isnull())


import pandas as pd
import numpy as np

# ─── Sample DataFrame with missing values ──────────────────────────────────────
data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age'  : [25, np.nan, 30],
    'Score': [85, 90, np.nan]
}
df = pd.DataFrame(data)

# ─── 1. Detect missing values ─────────────────────────────────────────────────
null_mask  = df.isnull()        # True/False mask of NaNs
null_count = df.isnull().sum()  # count of NaNs per column

# ─── 2. Remove missing data ───────────────────────────────────────────────────
df_drop_rows = df.dropna()          # drop rows containing any NaN
df_drop_cols = df.dropna(axis=1)    # drop columns containing any NaN

# ─── 3. Fill missing data ─────────────────────────────────────────────────────
df_fill_zero = df.fillna(0)                         # fill all NaNs with 0

df_fill_mean = df.copy()                            # fill specific column with mean
df_fill_mean['Age'].fillna(df['Age'].mean(), inplace=True)

df_ffill = df.fillna(method='ffill')   # forward‑fill from previous row
df_bfill = df.fillna(method='bfill')   # back‑fill from next row

# ─── 4. Replace specific values (including NaN) ───────────────────────────────
df_replace_nan  = df.replace(to_replace=np.nan, value='Missing')
df_replace_name = df.replace({'Charlie': 'Krish'})

# ─── Optional: print results to verify ────────────────────────────────────────
print("Original DataFrame:\n", df, "\n")
print("Null mask:\n", null_mask, "\n")
print("Null count per column:\n", null_count, "\n")
print("Rows without NaN:\n", df_drop_rows, "\n")
print("Filled with zeros:\n", df_fill_zero, "\n")
