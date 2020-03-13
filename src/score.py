import requests
from bs4 import BeautifulSoup


# Scrapes an ebay webpage and list the names of the items in the page


response = requests.get(
    "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR0.TRC0.A0.H0.TRS2&_nkw=phone&_sacat=0")
print("Status is ", response.status_code)
if response.status_code != 200:
    print("Error..")

else:

    print("Scraping...")

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.findAll("div", {"class": "s-item__wrapper clearfix"})
    print(len(items))
    for item in range(3):
        print(items[item].h3.text + "\n")
