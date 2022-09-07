import pandas as pd 

########################
### load in the data 
########################
patients = pd.read_csv('enrichment/example_data/patients.csv')
patients

medications = pd.read_csv('enrichment/example_data/medications.csv')

patients.columns
medications.columns

patients['Id']
medications['PATIENT']


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