import  requests
from bs4 import BeautifulSoup #scrapping
page=requests.get("https://forecast.weather.gov/MapClick.php?lat=42.9371&lon=-75.6107#.XoC0TphR3IU")
soup=BeautifulSoup(page.content,"html.parser")
#print(soup)
#print(soup.find_all("a"))
#week=soup.find(id='seven-day-forecast-container')
#print(week)
week=soup.find(id='seven-day-forecast-container')
items=week.find_all(class_="tombstone-container")
print(items)
#print(items[0].find(class_="period-name").get_text())


