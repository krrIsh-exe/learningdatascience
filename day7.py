"""📌 Why Handle Missing Data?
Real-world datasets are messy — some values are often missing (NaN = Not a Number).

We need to:

Detect missing values

Decide whether to remove or fill them"""

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