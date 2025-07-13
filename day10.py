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
