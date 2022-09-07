import pandas as pd
import datetime as dt
import uuid
import numpy as np


# load in messy data
df = pd.read_csv(
    'transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv')

df

# get a count of the number of rows and columns
countRows, countColumns = df.shape

# preview get random sample of 25 rows
df.sample(25)

# change countRows to full integer
tenPercent = int(countRows * 0.1)

sample_df_1 = df.sample(tenPercent)
sample_df_2 = df.sample(int(countRows * 0.1))


# clean the data
# list columns
list(df)


############## COLUMN NAMES ##############
############## COLUMN NAMES ##############
############## COLUMN NAMES ##############

df.columns
column_names = list(df)


# remove all special characters and whitespace ' ' from column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')  # regex
list(df)

# renaming columns
# rename the column, where the first value is the old name and the second value is the new name
df = df.rename(columns={'Code': 'billing_code'})
df

df = df.rename(columns={
    'emblemhealth_ghi_commercial': 'emblemhealth_ghi_commercial_mod',
    'emblemhealth_hip_medicare_advantage': 'emblemhealth_hip_medicare_advantage_mod',
})

# change all column names to lowercase
df.columns = df.columns.str.lower()

# change all column names to upper case
df.columns = df.columns.str.upper()

# replace all whitespace in column names with an underscore
df.columns = df.columns.str.replace(' ', '_')

# droping columns
# remember this is CASE SENSITIVE
df.drop(['billing_code'], axis=1, inplace=True, errors='ignore')
df.columns

############## REMOVING WHITESPACE ##############
############## REMOVING WHITESPACE ##############
############## REMOVING WHITESPACE ##############

# remove all whitespace for values within a specific column
df['x'] = df['x'].str.strip()
# remove all special characters and whitespace ' ' from a specific column
# regex # regex tutorial/info: https://www.w3schools.com/python/python_regex.asp;  https://www.regular-expressions.info/refquick.html
df['billing_code'] = df['billing_code'].str.replace('[^A-Za-z0-9]+', '_')


############## COLUMN TYPES ##############
############## COLUMN TYPES ##############
############## COLUMN TYPES ##############


# get list of column types
# want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
df.dtypes

# create a list of columns that are strings, and save as strings
strings = df.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = df.select_dtypes(include=['int64', 'float64']).columns
# create a list of columns that are dates, and save as dates
dates = df.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = df.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = df.select_dtypes(include=['object']).columns

# you would then manually go through each of these, and determine if the column
# type is appropriate for the data model you are creating

df['billing_code'] = df['billing_code'].astype(str)
df['billing_code'] = str(df['billing_code'])

# get billing_code type
df.dtypes


########## DATES ##########
########## DATES ##########
########## DATES ##########

# dealing with dates
# convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])
# convert date column to datetime format like this: '%Y-%m-%d'
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# convert date column to datetime format like this: '%Y_%M_%D'
df['date'] = pd.to_datetime(df['date'], format='%Y_%M_%D')
# convert date to quarter format
df['date'] = df['date'].dt.quarter
# convert date to year format
df['date'] = df['date'].dt.year
# determine if date is on weekday or weekend
df['date'] = df['date'].dt.dayofweek


########## MISSING DATA ##########
########## MISSING DATA ##########
########## MISSING DATA ##########

# get a count of missing values in each column
df.isnull().sum()

# replacing blank, empty cells with NaN
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)

# drop rows with missing values
df.dropna(inplace=True)  # drop rows with missing values

# droping specific rows
df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], axis=0,
        inplace=True)  # example of dropping rows


########## UNIQUE IDs ##########
########## UNIQUE IDs ##########
########## UNIQUE IDs ##########

# Creating UNIQUE IDs

# Example 1
# create a unique id for each row using uuid
df['id'] = df.apply(lambda x: uuid.uuid4(), axis=1)

# create a unique id for each row using uuid that contains 8 characters
df['id'] = df.apply(lambda x: uuid.uuid4().hex[:8], axis=1)

# Example 2
# create a function that will create a unique id for each row


def create_id():
    return uuid.uuid4()


# create a new column that will have a unique id for each row
df['id'] = df.apply(lambda row: create_id(), axis=1)
