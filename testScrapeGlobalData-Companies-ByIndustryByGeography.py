
from requests import get
from csv import writer
# import requests
from bs4 import BeautifulSoup
URL = "https://www.globaldata.com/companies/listing/search/?location=16220&industry=4800013&q[]=Canada%2520Mining&pageSize=10000&pageNumber=1&sortColumn=1&sortDirection=asc"

r = get(URL)

soup = BeautifulSoup(r.content,"html.parser")

# lock_tags = soup.find_all('lock-box')
# print(lock_tags)

# for locks in lock_tags:
#     locks.span.decompose()

# soup = BeautifulSoup(r.text,"lxml")
# soup.find('div', id="lock-box").decompose()
# soup.contents.find_all('div','lock-box')


element = soup.find('div', class_='lock-box')
print(element)
if element and 'class' in element.attrs:
    # Split the class attribute into individual classes
    classes = element['class']
    # .split()

    # Remove the desired class (e.g., 'my-class')
    if 'lock-box' in classes:
        classes.remove('my-class')

    # Join the modified classes back into a string
    new_class = ' '.join(classes)

    # Update the 'class' attribute of the element
    element['class'] = new_class    
print(element)

# get all tables
tables = soup.find_all('tbody')

# for result in soup.findAll('a'):
#     with open('afile.csv','w') as f:
#         csv_writer = writer(f)
#         csv_writer.writerow(result)
f = open('file.txt', 'w')
f.write(soup.text)
f.close()       


# loop over each table
for num, table in enumerate(tables, start=1):

    # create filename
    filename = 'table-%d.csv' % num

    # open file for writing
    with open(filename, 'w') as f:

        # store rows here
        data = []

        # create csv writer object
        csv_writer = writer(f)

        # go through each row
        rows = table.find_all('tr')
        for row in rows:

            # write headers if any
            headers = row.find_all('th')
            if headers:
                csv_writer.writerow([header.text.strip() for header in headers])

            # write column items
            columns = row.find_all('td')
            csv_writer.writerow([column.text.strip() for column in columns])

# print(tables)

# s = scrapelib.Scraper(requests_per_minute=10)
# page = s.get(URL)
# print(page.text)


# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")

# tables = soup.findAll("table")
# print(tables.__annotations__)

# for table in tables:
#      if table.findParent("table") is None:
#          print(str(table))

# print(page.text)

# # Didn't work for unknown reason
# import pandas as pd
# url = 'https://www.globaldata.com/companies/listing/search/?location=16220&industry=4800013&q[]=Canada%2520Mining&pageSize=100&pageNumber=1&sortColumn=1&sortDirection=asc'
# dfs = pd.read_html(url)
# print(len(dfs))