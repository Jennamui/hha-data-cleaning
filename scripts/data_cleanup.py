#import packages
from multiprocessing.reduction import duplicate
import pandas as pd
import datetime as dt
import uuid
import numpy as np

#Load in dataset
df = pd.read_csv('data/School_Learning_Modalities.csv')

#Print the number of columns and rows
df.shape

#List the column names
list(df)

#Remove white space from column names and replace with an underscore
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
list(df)

df.dtypes

# create a list of columns that are objects, and save as objects
objects = df.select_dtypes(include=['object']).columns

#Convert "Week" column to datetime
df['Week'] = pd.to_datetime(df['Week'])

# create a list of columns that are dates, and save as dates
dates = df.select_dtypes(include=['datetime64[ns]']).columns

#Convert to year, month, day format
df['Week'] = pd.to_datetime(df['Week'], format='%Y-%m-%d')

#Count the missing values in each column
df.isnull().sum()

#Replace missing values with NaN
df.replace(to_replace='', value=np.nan, inplace=True)

#Find any duplicate rows
duplicate = df.duplicated()

#Delete duplicate rows
df.drop_duplicates()

#Create new column called "modality_inperson" based on "Learning_Modality" Column with function that recodes "True" for "In Person" and "False" for "Remote" or "Hybrid"
df['modality_inperson'] = np.where(df['Learning_Modality']!= 'In Person', False, True)
df.head()

#Save clean version to csv file
df.to_csv('/Users/jennamui/Downloads/Learning_modalities_clean.csv')
