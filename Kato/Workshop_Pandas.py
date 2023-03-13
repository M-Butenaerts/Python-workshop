import pandas as pd

df = pd.read_excel(r'C:\Users\vanak\OneDrive\Documenten\TU Delft\Python-workshop\Python workshop (Responses) (1).xlsx')


print('info',df.info())
print('top x rows',df.head(6))
print(df.keys())


# for i in range(13,19):
#     df.drop(columns=[f'Unnamed: {i}'], inplace = True)
#
# print(df.keys())
print(df['Naam'])
