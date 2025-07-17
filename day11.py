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
