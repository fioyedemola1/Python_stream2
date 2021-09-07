import requests
from bs4 import BeautifulSoup
import requests
url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
items = soup. find_all('div',class_="propertyCard-section")


for item in items:
     Title = item.find('h2', class_="propertyCard-title").text
     Location = item.find('address', class_="propertyCard-address").text
     Price = item.find('div', class_="propertyCard-priceValue").text
     info = [Title, Location,Price,Contact]
     Contact = item.find('a', class_="propertyCard-contactsPhoneNumber").text
     print(info)



