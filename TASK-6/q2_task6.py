import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv")

print(df.iloc[:,3:4].isnull().values,df.iloc[:,6:7].isnull().values,df.iloc[:,30:32].isnull().values)

imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

imputer.fit(df.iloc[:,3:4].values)
df.iloc[:,3:4]=imputer.transform(df.iloc[:,3:4].values)

imp = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
imp.fit(df.iloc[:,30:32].values)
df.iloc[:,30:32]=imp.transform(df.iloc[:,30:32].values)
imp.fit(df.iloc[:,6:7].values)
df.iloc[:,6:7]=imp.transform(df.iloc[:,6:7].values)

print(df.isnull())

print(df)

print(df.iloc[:,3:4].values,df.iloc[:,6:7].values,df.iloc[:,30:32].values)

print(df.iloc[:,3:4],df.iloc[:,6:7],df.iloc[:,30:32])

