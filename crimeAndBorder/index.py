from bs4 import BeautifulSoup
from urllib.request import urlopen
import math
import csv
'''
There is a continuous discussion about whether or not the [illegal]
immigrants infiltrating the USA from Mexico positively affect the
crime rate in the border neighborhoods. Your assignment is to cast
some light on the situation using data from Wikipedia.
Write a program that shall:

1. Download and extract crime-related data (namely, the total violent crime rate
per 100,000 people) from the major US cities from the List of US cities by crime
rate. https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate

2. For each city, follow the link to its Wikipedia page and extract its
coordinates. Calculate the distance to the border as the smallest distance from
each city to San Ysidro, Yuma, Tucson, El Paso, Laredo, Del Rio, and
Brownsville, TX. You are allowed to hardcode the coordinates of these locations.
Use the great- circle distance formula.

3. Save the city names, crime rates, and smallest distances to the border in a 3-
column CSV file.

4. Calculate and display the correlation between the two numbers (use scipy.corrcoeff()).

Finally, scatter plot crime rates against the distances. You can use
Excel, Google Sheets, LibreOffice, or matplotlib. Add a trend line if
you want. Write a one-page report that explains in layperson’s terms
the procedure of your discovery, your findings (especially the
correlation), and their significance. Include the scatter plot in the
report. For the report, use MS Word, Google Docs, or LibreOffice.
Save each downloaded HTML document into the directory data. If the directory does not exist, create it. If a needed document has been previously downloaded, it shall be retrieved from the file, not from the Web1.
1 Consider writing function getDocument(URL) that checks if the document has been stored in the data directory. If it is, the function shall read it from the file. If it is not or the directory does not exist yet, the function shall create the directory, download the document, save it to an appropriately named file, and return its content. Do not use any absolute file paths in your code, as I will not be able to reproduce your results.
        Spring 2020 Data Science CMPSC-310
Suffolk University Math & CS Department
You must use modules CSV and BeautifulSoup. You will probably need
module urllib. You are not allowed to use NumPy or Pandas. The use of
module matplotlib is optional.
Deliverable (to be submitted to BlackBoard): Your code and the
report. Do not include the HTML files.
'''

def main():
    borderCoordinates = [
        # Brownsville, Texas
        ['25°55′49″N', '97°29′4″W'],
        # El Paso
        ['31°45′33″N', '106°29′19″W'],
        # Yuma, Arizona
        ['32°41′32″N', '114°36′55″W']
    ]
#each city to San Ysidro, Yuma, Tucson, El Paso, Laredo, Del Rio, and
#Brownsville, TX. You are allowed to hardcode the coordinates of these locations.
    wikiURL = "https://en.wikipedia.org"
    URL     = wikiURL + "/wiki/List_of_United_States_cities_by_crime_rate"
    with urlopen(URL) as url:
        soup = BeautifulSoup(url,"lxml")
    table = soup.find("table")
    data  = table.find_all("tr")
    # We extract some general information about the city for later reuse.
    # Wikipedia has not labelled their columns with class names, so we need to
    # manually write them, and target their numeric indices.
    #
    # We need the URL to retrieve the page for that city, and to calculate its
    # distance to the border.
    fieldNames = ["state", "city", 'url', "crime rate"]
    fileName   = "crimeRatesByBorderProximity.csv"
    lis_array  = []
    for link in data:
        # We can skip this data if it is a column without a linked city.
        # Otherwise we have no subsequent data to parse the distance to the
        # border.
        cityLink = link.contents[3].a
        if None == cityLink:
            continue;
        # We find the citySuffix by parsing down through each table cell. They
        # are not labelled, so we need to look at what the object contains to
        # find the numeric index.
        citySuffix = link.contents[3].a.get('href')
        td         = link.find_all('td')
        row        = [i.text for i in td]
        with urlopen(wikiURL + citySuffix) as cityURL:
            citySoup = BeautifulSoup(cityURL, 'lxml')
        # Once we have the city page, we can pull the geographic coordinates for
        # it. We will use them to find its distance to the nearest border.
        # We convert them to radians right away, because we are not required to
        # print the coordinates, but we need radians for the formula.
        cityLatitudeString = (
            citySoup.find('span', {'class': 'latitude'}).contents[0]
        )
        # We now need to parse the coordinate into decimal format, since it is
        # currently in imperial: 30°41′40″N
        cityLatitude = int(cityLatitudeString[0:2])
        cityLatitude = cityLatitude + int(cityLatitudeString[3:5]) / 100
        cityLatitude = cityLatitude + int(cityLatitudeString[6:8]) / 1000
        cityLatitude = math.radians(cityLatitude)
        # Here is the same for longitude.
        cityLongitudeString = (
            citySoup.find('span', {'class': 'longitude'}).contents[0]
        )
        cityLongitude = int(cityLongitudeString[0:2])
        cityLongitude = cityLongitude + int(cityLongitudeString[3:5]) / 100
        cityLongitude = cityLongitude + int(cityLongitudeString[6:8]) / 1000
        cityLongitude = math.radians(cityLongitude)
        # With the coordinates in hand, we use the great circle formula to
        # calculate the distance, and find the closest border town.
        # https://en.wikipedia.org/wiki/Great-circle_distance
        borderDistance = 0
        for borderTown in borderCoordinates:
            borderXRadians = math.radians(borderTown[1])
            borderYRadians = math.radians(borderTown[0])
            deltaSigma = math.acos(
                math.sin(cityLongitude) * math.sin(borderXRadians)
                + math.cos(math.abs(cityLatitude - borderYRadians))
                * math.cos(cityLongitude) + math.cos(borderXRadians)
            )
            if ((borderDistance == 0)
            or (borderDistance < circleRadians * deltaSigma)
            ):
                borderDistance = circleRadians * deltaSigma
        lis_array.append([row[0], row[1], borderDistance, row[3]])
    with open(fileName, "w") as csvFile:
        csvwriter = csv.writer(csvFile)
        csvwriter.writerow(fieldNames)
        csvwriter.writerows(lis_array)


if __name__=="__main__":
    main()


