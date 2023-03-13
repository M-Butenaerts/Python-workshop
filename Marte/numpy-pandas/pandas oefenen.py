import pandas as pd

# df = datafrme (convention naming)
# r voor string anders moet je overal \\ gebruiken waar \ staat

df = pd.read_excel(r'C:\Users\Marte\PycharmProjects\Python-workshop\Python workshop (Responses) (1).xlsx')
print(df.info())
print(df.keys())
#print(df['Naam'])

#for i in range(13, 19):
#    df.drop(columns=[f'Unnamed: {i}'], inplace=True) # inplace.trus= df naam behouden maar kollom wel droppen
# inplace zodat je niet df.['xxx'] = df.[''].operatie moet doen
df['Leeftijd'] = df['Leeftijd'] - 2
print(df['Leeftijd'])


