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

print(df.isnull())