import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.python.org/jobs/")
data= BeautifulSoup(response.text,"html.parser")
positions = data.find_all("span",attrs={"class":"listing-company-name"})
for position in positions:
    print(position.find("a").text.strip())
    
    