import pandas as pd

data = pd.DataFrame({'EmployeeName': ['Callen Dunkley', 'Sarah Rayner', 'Jeanette Sloan', 'Kaycee Acosta', 'Henri Conroy', 'Emma Peralta', 'Martin Butt', 'Alex Jensen', 'Kim Howarth', 'Jane Burnett'],
                    'Department': ['Labs', 'Nursing', 'Nursing', 'HR', 'HR', 'HR', 'Data Science', 'Data Science', 'Labs', 'Data Science'],
                    'HireDate': [2010, 2018, 2012, 2014, 2014, 2018, 2020, 2018, 2020, 2012],
                    'Sex': ['M', 'F', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'F'],
                    'Birthdate': ['04/09/1982', '14/04/1981', '06/05/1997', '08/01/1986', '10/10/1988', '12/11/1992', '10/04/1991', '16/07/1995', '08/10/1992', '11/10/1979'],
                    'Weight': [78, 80, 66, 67, 90, 57, 115, 87, 95, 57],
                    'Height': [176, 160, 169, 157, 185, 164, 195, 180, 174, 165],
                    'YearsEmployeed': [2, 1, 0, 1, 1, 0, 2, 0, 3, 1]
                    })

df_wide = pd.DataFrame(
  {"student": ["Andy", "Bernie", "Cindy", "Deb"],
   "school":  ["Z", "Y", "Z", "Y"],
   "english": [10, 100, 1000, 10000],  # eng grades
   "math":    [20, 200, 2000, 20000],  # math grades
   "physics": [30, 300, 3000, 30000]   # physics grades
  }
)

df_wide_2 = pd.DataFrame(
  {"hospital": ["Stony Brook", "Mount Sinai", "Northwell", "HSS"],
   "multisite":  ["Y", "Y", "Y", "N"],
   "patient_nps": [70, 80, 85, 70],  
   "revenue_in_millions":    [500, 1400, 1000, 1800],  
   "careprovider_nps": [85, 90, 83, 78]   
  }
)