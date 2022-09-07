import pandas as pd
from tableone import TableOne, load_dataset

##### DATASET 1 #####
example_data = load_dataset('pn2012')
# # littlerecode death where 0 is alive and 1 is dead
# example_data['death'] = example_data['death'].replace(0, 'alive')
example_data.dtypes
example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']
example_data_categorical = ['ICU', 'death']
example_data_groupby = ['death']
example_data_labels={'death': 'mortality'}
exampleTab1 = TableOne(example_data, columns=example_data_columns, 
    categorical=example_data_categorical, groupby=example_data_groupby, 
    rename=example_data_labels, pval=False)
exampleTab1
print(exampleTab1.tabulate(tablefmt = "fancy_grid"))
exampleTab1.to_csv('descriptive/example1/data/test.csv')



##### DATASET 2 #####
my_data = pd.read_csv('descriptive/example1/data/data.csv')
df2 = my_data.copy()
df2.dtypes
list(df2)
df2.head(5)
df2['Smoke']
df2_columns = ['Age', 'HR', 'Group', 'sBP', 'Smoke']
df2_categories = ['Smoke', 'Group']
df2_groupby = ['Smoke']
# df2['Vocation'].value_counts()
df2_table1 = TableOne(df2, columns=df2_columns, 
    categorical=df2_categories, groupby=df2_groupby, pval=False)
print(df2_table1.tabulate(tablefmt = "fancy_grid"))
df2_table1.to_csv('descriptive/example1/data/test2.csv')