#Reshaping DataFrames (melt, stack, unstack) ← next

import pandas as pd

data = {
    'Name': ['Krish', 'Vraj'],
    'Math': [85, 90],
    'Science': [95, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 🔄 Melt it
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Math', 'Science'],
                    var_name='Subject', value_name='Score')

print("\nMelted DataFrame:")
print(melted_df)


# pd.melt(
#     frame,             # ← Your original DataFrame
#     id_vars=None,      # ← Columns to keep fixed (like title, name)
#     value_vars=None,   # ← Columns you want to melt (optional)
#     var_name=None,     # ← Name of the new "feature name" column
#     value_name='value' # ← Name of the new "value" column
# )


#-----------------------------------------------------------------------------------------------------------------------------------


# 2. stack() and unstack() — Pivot levels in index/columns
# ✅ stack():
# Moves columns into index (compresses columns down into rows).

# ✅ unstack():
# Moves index into columns (opposite of stack).


df = pd.DataFrame({
    'Name': ['Krish', 'Vraj'],
    'Subject': ['Math', 'Science'],
    'Score': [85, 95]
})

# Set multi-index
df = df.set_index(['Name', 'Subject'])
print("MultiIndex DataFrame:")
print(df)

# 🔻 Stack
stacked = df.stack()
print("\nStacked:")
print(stacked)

# 🔼 Unstack
unstacked = df.unstack()
print("\nUnstacked:")
print(unstacked)


# Function	Action	Use Case
# melt()	Wide ➡ Long	Tidy messy data with many columns                    (Converts collumns in to rows)
# pivot()	Long ➡ Wide	Opposite of melt                                     (Converts rows in to columns)
# stack()	Column → Index	Collapse levels for hierarchical data
# unstack()	Index → Column	Expand levels into columns


# practice session 
import pandas as pd
mdf = pd.DataFrame ({
    'name': ['krish','anakin'],
    'score':[50,78],

    
})
print('mdf')
mdf =mdf.set_index(['name','score'])
print(mdf)