#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import numpy as np
import pandas as pd
import json


# # Origin

# In[2]:


#Enter File Path
file = '/data/clean/refugee_origin_d3.csv'

#Convert to Dictionary
dataframe = pd.read_csv(file)
year = dataframe['Year']
dataframe.columns = ['Year', 'Country1', 'Country2', 'Country3', 'Country4', 'Country5']
dataframe = (dataframe/1000)
dataframe['Year'] = year
dictionary = dataframe.to_dict(orient='records')

#Export text File
with open('data/clean/origin.txt', 'w') as file:
     file.write(json.dumps(dictionary))


# # Asylum

# In[3]:


#Enter File Name
path = '/data/clean/'
files = ['refugee_asylum_afghanistan.csv', 'refugee_asylum_iraq.csv', 'refugee_asylum_somalia.csv', 'refugee_asylum_sudan.csv', 'refugee_asylum_syria.csv']

for file in files:
    #Convert to Dictionary
    dataframe = pd.read_csv(path+file)
    year = dataframe['Year']
    dataframe.columns = ['Year', 'Country1', 'Country2', 'Country3', 'Country4', 'Country5']
    dataframe = (dataframe/1000)
    dataframe['Year'] = year
    dictionary = dataframe.to_dict(orient='records')

    #Export text File
    with open(('data/clean/' + (file.split('_')[2].split('.')[0] + '.txt')), 'w') as file:
         file.write(json.dumps(dictionary))

