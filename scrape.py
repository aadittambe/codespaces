###
# Scraper borrowed from IRE's web scraping tutorial: https://github.com/ireapps/teaching-guide-python-scraping
###

# Import libraries
import bs4
import csv
import requests

# Define URL, make the soup
URL = 'http://www.dllr.state.md.us/employment/warn.shtml'
warn_page = requests.get(URL)
soup = bs4.BeautifulSoup(warn_page.text, 'html.parser')

# Find table
table = soup.find('table')
rows = table.find_all('tr')

# Define our headers
HEADERS = [
    'warn_date',
    'naics_code',
    'biz',
    'address',
    'wia_code',
    'total_employees',
    'effective_date',
    'type_code'
]

# Loop over rows and write out data a CSV
with open('warn-data.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(HEADERS)
    for row in rows[1:]:
        cells = row.find_all('td')
        values = [c.text.strip() for c in cells]
        writer.writerow(values)