# 29-9-18 Gareth
# BS scraping WORKS
# Awesome program
# https://pythonprogramming.net/tables-xml-scraping-parsing-beautiful-soup-tutorial/?completed=/navigating-pages-scraping-parsing-beautiful-soup-tutorial/

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.table

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

# now scrping into a pandas df
# change the URL to scrape ANY table 
# e.g. TRY the following:

# https://pythonprogramming.net/parsememcparseface/
# http://espn.go.com/college-football/bcs/_/year/2013
# https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
# https://data.gov.ie/dataset/cinemas/resource/1baf7193-4805-4cbc-8b41-273afb8ab340

import pandas as pd

dfs = pd.read_html('http://espn.go.com/college-football/bcs/_/year/2013',header=0)
for df in dfs:
    print(df)
