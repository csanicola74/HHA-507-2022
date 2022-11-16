# Competition Rules 

## Background 
- This is a dataset that provides information related to no shows for clinical appointments across small healthcare clinics across the country. 
Please create a new **PRIVATE REPO** called `ahi-competition`. The goal of this competition is to better understand NO SHOWS. In this project you will be required to do research on no-shows, determine how to enhance the existing dataset with new public data, and then peform traditional and non-traditional approaches to understand what factors may predict no shows, general no-show trends (persona groups - e.g., old, poor, with low tech literacy), or a predictive ML model that can be deployed into production.  
- The dataset that is provided is a small sample of 50,000 random encounters of people that showed up for their appointments, and a random sample of 50,000 encounters of people that did not show up for their appointments 

### Part 0: Expected folder structure: 
- /research 
- /data
- /scripts 
- /insights 

### Part 1: Research 
Find at least 3 research articles (e.g., Pubmed) that can be used to inform about what potential variables might be of interest for predicting if a patient shows or does not show to a appointment 
- What you find should be placed into a `/research` folder inside of your github repo 

### Part 2: Enhancement 
Find at least one external dataset (that is public) that can be brought in and merged with the existing dataset. The goal is to enhance or enrich the dataset with either sociodemogrpahic, clinical, or other non-traditional data sources that you think might impact, or be a significant predictor of whether a patient shows or does not show based on your Part 1 research that is performed 
- the enhancement dataset(s) or API references should be placed/references into the `/data` folder inside of your github repo with appropriate naming conventions
- the scripts that you write to merge/transform the enhanced dataset and original data file should be placed within `/scripts` folder 
- there should be a new `master.csv` file that is created and stored in the `/data` folder 

### Part 3: Visualization based on descriptives
Create at least one .py script that utilizes Streamlit to provide visualizations of the baseline data. There should be comparisons that focus on key descriptive differences that may or may not exist between persons that showed versus did not show for their appointments (e.g., gender differences? location differences? weather differences? X differences?)

### Part 4: Statistics and ML 
Perform at least one traditional statistical test (in either R or python or SATA or SAS) and one ML test (e.g., ML JAR).
- place your output of these tests inside of the `/insights` folder 
