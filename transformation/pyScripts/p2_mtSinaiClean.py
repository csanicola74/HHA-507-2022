import pandas as pd 

# load the data 

# load csv file and remove first two rows
mountSinai = pd.read_csv('transformation/dataFiles/131624096_mount-sinai-hospital_standardcharges.csv')


## mountSinai clean 
df = mountSinai

## list of current rows 
list(df)

## STEP 1 - Find and Rename Columns 
## rename columns
df.rename(columns={'CAMPUS':'hospital_name', 
            'Payer/Plan Name':'insurance_type', 
            'DRG/CPT/HCPCS Code':'code', 
            'DRG/CPT/HCPCS Description':'code_description',
             'Negotiated Charge':'cost_negotiated', 
             'Minimum Negotiated Charge':'cost_minimum',
             'Maximum Negotiated Charge': 'cost_maximum'}, inplace=True)

## STEP 2 - Delete the columns that we do not require withi nour data model 
keepVars = ['hospital_name', 'insurance_type', 'code', 'code_description', 'cost_negotiated', 'cost_minimum', 'cost_maximum']
df = df[keepVars]

## save the clean Version to a csv file in cleanData
df.to_csv('/Users/hantswilliams/Documents/development/python_projects/hospitalPriceline/cleanData/mountSinai_clean.csv')



