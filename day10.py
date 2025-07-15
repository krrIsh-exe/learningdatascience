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


# map function practice

import pandas as pd 

df = pd.DataFrame({
    'Name' :['krish','vraj','kylo'],
    'Score':[50,75,70]
})

df['Score'] =df['Score'].map(lambda x:x+15)  # python does not allows to use assignment operator inside a print function
print(df)


#apply function practice

import pandas as pd 

dfa=pd.DataFrame({
    'name':['kris' ,'vraj','anakin']
})

dfa['name_len']= dfa['name'].apply(len)
print(dfa)

# apply map function practice

dfam=pd.DataFrame({
    'maths':[80 ,90,70],
    'science':[50,38,78]
})

print(dfam.applymap(lambda x :x+5))