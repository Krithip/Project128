from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
soup = bs(page.text, 'html.parser')
starTable = soup.find_all('table')
tempList = []
tableRows = starTable[7].find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    tempList.append(row)
starName = []
distance = []
mass = []
radius = []
for i in range(1, len(tempList)):
    starName.append(tempList[i][0])
    distance.append(tempList[i][5])
    mass.append(tempList[i][7])
    radius.append(tempList[i][8])
df = pd.DataFrame(list(zip(starName, distance, mass, radius, )),columns = ["Star_Name", "Distance", "Mass", "Radius"])
print(df)
df.to_csv('dwarfStar.csv')