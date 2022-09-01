import pandas as pd 

# load the data
stonybrook = pd.read_csv('transformation/dataFiles/113243405_StonyBrookUniversityHospital_standardcharges.csv')

## looking at the data frame, it is currently in WIDE format, we want to make it STACKED format
## so first lets get a name of the columns 
columnNames = list(stonybrook)

idVars = columnNames[:8] # this is identify the key variables that we want to keep to designate what is the lowest unit of each row
valueVars = columnNames[8:] #these are the idential variables that we want to 'stack' 

## transofmring with the melt function from a wide dataframe to a stacked dataframe
stonybrook_modified = stonybrook.melt(id_vars=idVars, value_vars=valueVars)

