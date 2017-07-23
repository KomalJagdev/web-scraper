## 
##
##Python script to scrape all urls from a website and save it into a csv file.
##


from bs4 import BeautifulSoup
import requests
import csv

url = input("Enter a website:")
r = requests.get(url)                   
data = r.text
soup = BeautifulSoup(data, 'html5lib')
# print(soup)

with open('web_scraper.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for link in soup.find_all('a'):
        csvwriter.writerow([link.get('href')])
