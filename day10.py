# 📘 Topic 10: Applying Functions in Pandas

# 🔧 Main Tools:
# map() → for Series (single column)

# apply() → for Series or entire DataFrame

# applymap() → for every cell in a DataFrame (only numeric/string)


# 1️⃣ map() – Apply to Single Column


import pandas as pd

df = pd.DataFrame({
    'Name': ['Krish', 'Vraj', 'Varun'],
    'Score': [90, 80, 70]
})

# Add 5 bonus marks
df['Score'] = df['Score'].map(lambda x: x + 5)

print(df)

# 🔄 apply() — Works on Series or DataFrame

import pandas as pd

df = pd.DataFrame({
    'Name': ['Krish', 'Vraj', 'Varun']
})

# Count number of letters in each name
df['Name_Length'] = df['Name'].apply(len)
print(df)


# 🎯 applymap() — Works only on DataFrame

df = pd.DataFrame({                                   #it does not works on series
    'Math': [70, 80, 90],
    'Science': [60, 75, 85]
})

# Add 10 bonus marks to every cell
print(df.applymap(lambda x: x + 10))
