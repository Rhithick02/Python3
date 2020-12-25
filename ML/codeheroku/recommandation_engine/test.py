import pandas as pd 

df = pd.read_csv('ds', index_col = 0)
# df = df.fillna(0)
df = df.dropna(thresh = 1, axis = 1)
print(df)