import pandas as pd

df = pd.read_excel(r'C:\Users\oscar\PycharmProjects\Python-workshop\Python workshop (Responses) (1).xlsx')

print(df.info()) #get general info of your dataframe

for i in range(13,19):
    df.drop(columns=[f'Unnamed: {i}'],inplace=True)
    
# df.dropna(inplace=True)

print(df.iloc[13,:])










