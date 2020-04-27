#Patrick Willison
#willispd@mail.uc.edu
#this webscraper will take data from the books.toscrape website and display the html elements
import requests, re 
from bs4 import BeautifulSoup

data = requests.get ("http://books.toscrape.com/").content
soup=BeautifulSoup(data,"html.parser")
print("here is a list of books!")
for title in soup.find_all('title'):print(title)#gets the title 
for header in soup.find_all('h1'):print(header) #gets the header
for books in soup.find_all('div'):print(books) #gets the whole webpage