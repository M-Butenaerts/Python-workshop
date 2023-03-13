import pandas as pd

df = pd.read_excel(r'C:\Users\rune\OneDrive\Documents\GitHub\Python-workshop\Python workshop (Responses) (1).xlsx')

df.dropna(inplace=True)
print(df.info())

#watafack