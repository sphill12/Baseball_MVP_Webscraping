'''Import necessary libraries'''
from bs4 import BeautifulSoup as bs
import regex
import requests
import pandas
'''loading wikipedia MVP webpage'''
r = requests.get("https://en.wikipedia.org/wiki/Major_League_Baseball_Most_Valuable_Player_Award")
print('hello')
soup = bs(r.content, 'html.parser')
print(soup.prettify())
header = soup.find('h2')
