from bs4 import BeautifulSoup
import requests

# Create output csv file to write to
File = open("out.csv", "a")

# Declare headers so not seen as spam by web hosts
HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) 
                AppleWebKit/537.36 (KHTML, like Gecko) 
                    Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

