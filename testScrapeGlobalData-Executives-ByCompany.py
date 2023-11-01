
from requests import get
from csv import writer
import csv
# import requests
from bs4 import BeautifulSoup
listURLs = []
with open('20231025 Canada Mining+ URLs Only.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        listURLs.append(row)
f.close()
# listURLs = csv.reader('listGlobalData-CompanyURLs.csv').text
URL = "https://www.globaldata.com/company-profile/pan-american-silver-corp/executives/"

for item in listURLs:
    URL = item[0]
    print(URL)
    r = get(URL)

    soup = BeautifulSoup(r.content,"html.parser")

    # soup.find('div', class_="grid-x grid-margin-x grid-margin-y").select()
    company = soup.find('title').text
    companyend = company.find(' Executive')
    company = company[:companyend]
    people = soup.find_all(class_="card person unbound")

    filename = 'executives-%s.csv' %company
    with open(filename,'w',newline='') as f:
        csv_writer = writer(f)
        for person in people:
            columns = person.find_all(True, {'class':['name','position','position-type']})
            # row = ""
            # for column in columns:
            #     row = row + "," + column.text
            #     print(row)
            csv_writer.writerow([column.text.strip() for column in columns])