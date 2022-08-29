import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files


### CSV to DataFrame
## import local CSV file into a dataframe 
df = pd.read_csv('ingestion/example_files/csv/synthetic/conditions.csv') ## read csv file
## import local CSV with ASCII encoding into a dataframe
df = pd.read_csv('ingestion/example_files/csv/synthetic/conditions.csv', encoding='ascii') ## read csv file
## import local CSV with UTF-8 encoding into a dataframe
df = pd.read_csv('ingestion/example_files/csv/synthetic/conditions.csv', encoding='utf-8') ## read csv file


### JSON 
## import local JSON file into a dataframe // 
df = pd.read_json('ingestion/example_files/json/Encounter-example-home.json') ## read json file, gives error of non-Series mixing dicts and series
## give orient command to specifiy structure // https://pandas.pydata.org/docs/reference/api/pandas.read_json.html  
df = pd.read_json('ingestion/example_files/json/Encounter-example-home.json', orient='index') ## read json file, gives error of non-Series mixing dicts and series
## import local JSON using json 
f = open('ingestion/example_files/json/Encounter-example-home.json') ## open json file
f_data = json.load(f) ## load json file
f_data ## print json file
f_data.keys() ## show keys in json file
f_data['status'] ## show specific key in json file
f_data['participant'] ## this is showing us that there is an array 
f_data['participant'][0]['period'] ## go into first value (and only 'row' of array), and show specific key in json file


### TXT file 
## import local TXT file into a dataframe
df = pd.read_csv('ingestion/example_files/text/patient.txt', sep='\t') ## read txt file
df
## import local TXT using open function, without specific separator
f = open('ingestion/example_files/text/patient.txt') ## open txt file
f_data = f.read() ## read txt file


### MICROSOFT FORMATS 
## import local xls file
df = pd.read_excel('ingestion/example_files/xls_xlsx/AHQDataFile2016.xls') ## read xls file
df
## get tab names in xlsx file
xls = xlrd.open_workbook('ingestion/example_files/xls_xlsx/AHQDataFile2016.xls', on_demand=True)
xls.sheet_names()
## import local xlsx file
df = pd.read_excel('ingestion/example_files/xls_xlsx/AHQDataFile2016.xls', sheet_name='Surgeries') ## read xlsx file
df


### PDF FILES 
pdfFileObj = open('ingestion/example_files/pdfs/AZURE Official PDF - Microsoft Azure Essentials Fundamentals of Azure 2nd ed pdf.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)
# creating a page object
pageObj = pdfReader.getPage(0)
# extracting text from page
print(pageObj.extractText())


### HTML
## import local HTML file into a dataframe
df = pd.read_html('ingestion/example_files/html/FhirWebsite.html') ## read html file
## import local HTML file into a soup object
f = open('ingestion/example_files/html/FhirWebsite.html') ## open html file
f_data = bs4.BeautifulSoup(f.read(), 'lxml') ## read html file
print(f_data.prettify()) ## print html file
print(f_data.head) ## print html file head
print(f_data.title) ## print html file title
print(f_data.body) ## print html file body
## import local HTML file into a soup object
f = open('ingestion/example_files/html/Stony Brook University, New York.html') ## open html file
f_data = bs4.BeautifulSoup(f.read(), 'lxml') ## read html file
print(f_data.prettify()) ## print html file
print(f_data.head) ## print html file head
print(f_data.title) ## print html file title
print(f_data.body) ## print html file body
## import local HTML file into soup object for stonybrook medicine 
f = open('ingestion/example_files/html/Stony Brook Medicine | Stony Brook Medicine.html') ## open html file
f_data = bs4.BeautifulSoup(f.read(), 'lxml') ## read html file
print(f_data.prettify()) ## print html file
print(f_data.head) ## print html file head
print(f_data.title) ## print html file title
print(f_data.body) ## print html file body
## import local HTML file into soup object for stonybrook medicine 


### WEB REQUESTS
## get request for https://jsonplaceholder.typicode.com/posts // https://jsonplaceholder.typicode.com/ 
r = requests.get('https://jsonplaceholder.typicode.com/posts') ## get request
## load as json 
r_data = r.json() ## load request as json
## load into dataframe
df = pd.read_json(r_data) ## read json file


### SQLALCHEMY
## connect to sqlite database
engine = sqlalchemy.create_engine('sqlite:///ingestion/example_files/sqlite/hospital.db') ## create engine
## get a list of tables in the database
engine.table_names() ## get table names
## query the bacteria table and return the first 5 rows
engine.execute('SELECT * FROM bacteria LIMIT 5').fetchall() ## query table
## query the bacteria table return the first 5 rows using pandas 
bacteria_table = pd.read_sql('SELECT * FROM bacteria LIMIT 5', engine) ## query table
## read table
doctor_table = pd.read_sql('doctor', engine) ## read table from sqlite database


### PILOW
## import local image file into a pillow object
img = Image.open('ingestion/example_files/image/SBU_logo.png') ## read image file
## display image
img.show() ## display image
## image details 
print(img.format, img.size, img.mode)


### PYDUB
## import local audio file into a pydub object
audio = pydub.AudioSegment.from_file('ingestion/example_files/audio/sample_9seconds.mp3') ## read audio file
## play audio
play(audio) ## play audio


### PLAYSOUND
## import local audio file into a playsound object
playsound.playsound('ingestion/example_files/audio/sample_9seconds.mp3') ## play audio file


### GEOPANDAS
## import local geospatial file into a geopandas object
gdf = gpd.read_file('ingestion/example_files/geospatial/stations.geojson') ## read geospatial file
## display geospatial file
gdf.plot() ## plot geospatial file // hard to view in VSC, this is easier to see in spyder or a notebook  


### BIGQUERY
## first need to load api key that you created based on readme instructions
# connect to bigquery, be sure to update the name of your file, this is currently mine
client = bigquery.Client.from_service_account_json('ingestion/example_files/bigquery/caroline-507-c98b1afca13c.json') ## create bigquery client
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100") ## query public dataset
## get results
results = query_job.result() ## get results
## putresults into dataframe
df = pd.DataFrame(results.to_dataframe()) ## put results into dataframe
