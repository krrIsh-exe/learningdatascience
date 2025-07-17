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
