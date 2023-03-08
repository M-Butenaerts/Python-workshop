import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#Excel inlezen
# fname = r'C:\Users\oscar\PycharmProjects\Python-workshop\[templatefolder]\numpy-pandas\Python workshop (Responses).xlsx'
fname = r'Python workshop (Responses).xlsx'
df = pd.read_excel(fname) #read in the excel using a dataframe
# df = pd.read_excel(fname,names=list(range(1,14)))

df2 = df.copy() #Get a copy for later on.

#Hoe ziet mijn datafram eruit?
print(df.head()) #get first five values
print(df.shape)  # get the #rows and #columns
print(f'\ntitle of the columns:\n{df.keys()}')  #get the keys
# print(df['Naam'])
print(df.info()) #get general info of your dataframe

###-----------------Basics----------------------
#Basic operations
df['Leeftijd'] += 5
df['Leeftijd'] /= 2
print('show a different age \n',df['Leeftijd'])

#delete columns
df.drop(columns=['Naam','Voornaam'])
print(df.keys())

#add column
df['nieuwe leeftijd'] = df['Leeftijd']-5
print(df)

#rename a column
df.rename(columns={'Timestamp': 'tijdstempel'},inplace=True)
print('Here',df.keys())

#index row
print('Slicing the first 5 values\n',df.iloc[0:5])
print('Get the second row\n', df.iloc[1])
print('Get the first six quotes\n',df.iloc[0:6,6])

###-------------conditionals---------------------
#get only rows with young people
jonk_volk = df2[df2["Leeftijd"] <= 20]
print('Conditional df with all young people\n',jonk_volk)

jonk_volk = df2['Geslacht'][df2["Leeftijd"] <= 20]
print('Conditional df of gender with all young people\n',jonk_volk)

#Get only rows with old guys
old_guys = df2[(df2['Leeftijd']>22)&(df2['Geslacht']=='M')]
print('Conditional with old guys',old_guys)


###------------what to do with Nan Values?------------
#Delete Nan rows
print('Mensen die Niets kwijt willen:\n',df2['Voornaam'][df2['Wil je nog iets kwijt over het leven of dergelijke?'].isna()])
df2.dropna(inplace=True)
print(df2.shape)
print(df2)


#Replace Nan Values
df['Wil je nog iets kwijt over het leven of dergelijke?'].fillna('Ik ben te lui om iets te typen en zal nooit iets bereiken in mijn leven',inplace=True)
print(df.iloc[:,-2])



###-----------------working with time (pandas datetime)---------------------

#Get the people who submitted it before 7/03
date =  pd.to_datetime('2023-03-07 16:00')
print(df2[df2['Timestamp']<date])

