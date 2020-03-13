import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
my_URL = "http://google.com"

uClient = uReq(my_URL)
page_html = uClient.read()
uClient.close()

soup = BeautifulSoup(page_html, "html.parser")
# print(soup.h1)
