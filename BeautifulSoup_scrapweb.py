Scraping_HTML_data wirh_beautiful_soap# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
spans = soup('span')
numbers = []
for span in spans:
  numbers.append(int(span.string))
  
print sum(numbers)
Status API Training Shop Blog About