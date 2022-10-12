import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://github.com/trending')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


# get the text from each repo
descriptions = soup.find_all('p',class_='col-9 color-fg-muted my-1 pr-4')
output_descriptions = []
for i in descriptions: #for x in y: 
    print(i.text)
    data = i.text
    output_descriptions.append(data)

len(output_descriptions)
output_descriptions[1]
output_descriptions[3]


repo_stars = soup.find_all('a', class_='Link--muted d-inline-block mr-3')
for i in repo_stars:
    print('Count: ', i.text)

# get the programming language from each repo
p_langauge = soup.find_all('span',attrs={'itemprop': 'programmingLanguage'})
# for each item in p_langauge, print the text
for language in p_langauge:
    print(language.text)


# find each article where class='Box-row'
articles = soup.find_all('article', class_='Box-row')
# get length of articles
len(articles)



# get the div that contains data-hpc
articles = soup.find_all(attrs={"data-hpc":True})  ## way one 
articles = soup.find_all('div',attrs={'data-hpc':True}) ## way two 


### by looking at the website, can see this is where the info is stored: 
# <h1 class=h3 lh-condensed  ---- this is for the name of the repo 
# <p1 class=col-9 color-fg-muted my-1 pr-4 ---- this is for the description of the repo

# get the name of the repo and print it
repo_name = soup.find_all('h1',class_='h3 lh-condensed')

repo_names = []

for item in repo_name:
    name = item.text 
    # print('Part 1: Raw: ', name)
    ## clean name remove whitespace
    name = name.strip()   
    # print('Part 2: Updated: ', name)
    ## remove new line
    name = name.replace('\n','')
    # print('Part 3: Updated: ', name)
    ## remove all white space
    name = name.replace(' ','')
    # print('Part 4: Updated: ', name)
    repo_names.append(name)

len(repo_names)

for names in repo_names: 
    print(names)




# get the description of the repo and print it
repo_desc = soup.find_all('p',class_='col-9 color-fg-muted my-1 pr-4')

repo_descs = []
for item in repo_desc:
    print(item.text)
    desc = item.text
    print('Part 1: Raw: ', desc)
    ## clean name remove whitespace
    desc = desc.strip()
    print('Part 2: Updated: ', desc)
    ## remove new line
    desc = desc.replace('\n','')
    print('Part 3: Updated: ', desc)
    repo_descs.append(desc)
len(repo_descs)


list1 = repo_names 
list2 = repo_descs

# create dictionary
dictionary = {'names': list1, 'description': list2}

## put this together into a dataframe
df = pd.DataFrame({'names':repo_names,'descriptions':repo_descs})

df.to_csv('/Users/hantswilliams/Desktop/githubtrending.csv')