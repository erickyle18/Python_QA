from bs4 import BeautifulSoup

xml_file = "movies.xml"

with open(xml_file, "r", encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "xml")

    items = soup.find_all("year")
    print (items)
