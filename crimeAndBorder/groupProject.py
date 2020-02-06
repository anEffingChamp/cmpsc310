from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def main():
    URL = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate"
    with urlopen(URL) as url:
        soup = BeautifulSoup(url,"lxml")
    table = soup.find("table")
    data = table.find_all("tr")

    fieldNames = ["State", "City", "Distance", "Crime Rate"]
    fileName = "CrimeRate.csv"
    lis_array = []
    for link in data:
        td = link.find_all('td')
        row = [i.text for i in td]
        for i in row:
            lis_array.append([row[0],row[1],"",row[3]])
            break
    with open(fileName, "w") as csvFile:
        csvwriter = csv.writer(csvFile)
        csvwriter.writerow(fieldNames)
        csvwriter.writerows(lis_array)


if __name__=="__main__":
    main()


