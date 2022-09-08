import pandas as pd 

########################
### load in the data 
########################
patients = pd.read_csv('enrichment/example_data/patients.csv')
medications = pd.read_csv('enrichment/example_data/medications.csv')


patients_small = patients[['Id', 'BIRTHDATE', 'DRIVERS', 'SSN']]
print(patients_small.to_markdown())


patients.columns
medications.columns

patients['Id']
medications['PATIENT']


###############
### Below, we are going to take our medications table, and enrich it with some 
### patient information from our patients table.
###############

df_patients_small = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]
print(df_patients_small.sample(10).to_markdown())
df_patients_small.shape

df_medications_small = medications[['PATIENT', 'CODE', 'DESCRIPTION', 'BASE_COST', 'PAYER']]
print(df_medications_small.sample(10).to_markdown())
df_medications_small.shape

combined_df = df_medications_small.merge(df_patients_small, how='left', left_on='PATIENT', right_on='Id')
combined_df = pd.merge(df_medications_small, df_patients_small, how='left', left_on='PATIENT', right_on='Id')

combined_df.columns
### save to csv 
combined_df.to_csv('enrichment/example_data/combined_df.csv')
combined_df.shape

payers = pd.read_csv('enrichment/example_data/payers.csv')



####
med_df = medications[['PATIENT', 'PAYER', 'CODE']]

pay_df = payers[['Id', 'CITY', 'UNIQUE_CUSTOMERS']]
pay_df.rename(columns={'CITY': 'CITY_PAYER'}, inplace=True)

pat_df = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]

## First merge, will be between med_df and pay_df
med_pay_df = med_df.merge(pay_df, how='left', left_on='PAYER', right_on='Id')
med_pay_df = med_pay_df.drop(columns=['Id'])
med_pay_df.shape

## for the med_pay_df, we will drop duplicate rows based on PATIENT
med_pay_df_nodups = med_pay_df.drop_duplicates(subset=['PATIENT'])
med_pay_df_nodups
med_pay_df_nodups = med_pay_df_nodups.drop(columns=(['CODE']))

## final step, we will add med_pay_df_nodups to our pat_df dataframe
final_df = pat_df.merge(med_pay_df_nodups, how='left', left_on='Id', right_on='PATIENT')


######
patient_medication = df_patients_small.merge(df_medications_small, how='left', left_on='Id', right_on='PATIENT')
patient_medication.shape
# to csv 
patient_medication.to_csv('enrichment/example_data/patient_medication.csv')


##### load in payers 
payers_df = pd.read_csv('enrichment/example_data/payers.csv')
payers_df.shape
payers_df.head
payers_df['NAME']
payers_df.columns


payers_df_small = payers_df[['NAME', 'Id', 'AMOUNT_COVERED']]

patients_payers = df_patients_small.merge(payers_df_small, how='left', on='Id')
patients_payers.columns
patients_payers.to_csv('enrichment/example_data/patients_payers.csv')

########################
### merge examples 
# add medications to patients
########################
patients_simple = patients[['Id', 'SSN']]
medications_simple = medications[['PATIENT', 'DESCRIPTION']]

patients_medications = patients_simple.merge(medications_simple, 
            how='left', 
            left_on='Id', right_on='PATIENT')

print(patients_medications.head(5).to_markdown())

patients_medications = patients_medications.drop(columns=['PATIENT'])

########################
### concat examples 
########################

patient_sample_1 = patients.sample(n=10)
patient_sample_2 = patients.sample(n=10)

patients_s1_s2_concat = pd.concat([patient_sample_1, patient_sample_2])