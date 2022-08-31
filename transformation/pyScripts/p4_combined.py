import pandas as pd

## load the clean mtSInai file 
mtSinai = pd.read_csv('transformation/cleanData/mountSinai_clean.csv')

## load the clean stonyBrook file
stonyBrook = pd.read_csv('transformation/cleanData/stonyBrook_clean.csv')

## concat the two files since they have the same column names (e.g., variables)
combined = pd.concat([mtSinai, stonyBrook])