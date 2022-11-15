import pandas as pd

sparcs = pd.read_csv('autoML/datasets/data_sparcs.csv')

# create new var called sparcs_los that if length of stay is greater than 5 days, then long, else short
# convert sparcs['Length of Stay'] to numeric
sparcs['Length of Stay'] = pd.to_numeric(sparcs['Length of Stay'], errors='coerce')
sparcs['sparcs_los'] = sparcs['Length of Stay'].apply(lambda x: 'long' if x > 3 else 'short')
sparcs['sparcs_los'].value_counts()
sparcs.drop('Length of Stay', axis=1, inplace=True)
sparcs.columns

# jsut get values from sparcs_los
sparcs_los = sparcs['sparcs_los'].values

# convert array to list
list1 = ['1', '2', '3', '4', '5']
list2 = ['a', 'b', 'c', 'd', 'e']
dataframe = pd.DataFrame({'col1': list1, 'col2': list2})