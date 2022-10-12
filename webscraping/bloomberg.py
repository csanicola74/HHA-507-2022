import pandas as pd
import requests
from bs4 import BeautifulSoup

# get bloomberg page
original = requests.get('https://www.bloomberg.com/markets/stocks')
original
original.text

## we can see that it has detected we are not in a browser, and it is asking to perform a action 
"""
class="main__heading">We\'ve detected unusual activity from your computer network</h2>\n       
 <p class="continue">To continue, 
please click the box below to let us know you\'re not a robot.</p>\n       
 <div id="px-captcha"></div>\n    </section>\n    <section class="box">\n        
 <section class="info">\n            <h3 class="info__heading">Why did this happen?</h3>\n           
  <p class="info__text">Please make sure your browser supports JavaScript and cookies and that
   you are not blocking them from loading. For more information you can review 
   our <a class="info__link" href="/notices/tos">Terms of Service</a> and <a cl
"""

# load bloomberg page from example_html
with open('/Users/hantswilliams/Documents/HHA-507-2022/webscraping/example_html/bloomberg.html') as f:
    soup = BeautifulSoup(f, 'lxml')
    

print(soup.prettify())

# example1 
test = soup.find_all('tr', class_="data-table-row")
for i in test:
    print(i.text)

# example2 
test2 = soup.find_all('tr', class_="data-table-row")
name_output = []
for i in test2:
    names = i.find_all('div', class_="data-table-row-cell__link-block")[0].text
    print('name:', names)
    name_output.append(names)
name_output
len(name_output)

values_output = []
for i in test2:
    values = i.find_all('span', class_='data-table-row-cell__value')[0].text
    print('value:', values)
    values_output.append(values)
values_output
len(values_output)

df = pd.DataFrame({'ticker': name_output, 'ticker_value': values_output})
df