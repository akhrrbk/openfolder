# this is a web scraper that extracts the price from olcha.uz website
# built by github.com/akhrrbk

from bs4 import BeautifulSoup
import requests

url = "https://olcha.uz/oz/product/view/apple-iphone-14-pro"
print("the link is \t" + url)

results = requests.get(url)
# print(results)

doc = BeautifulSoup(results.text, "html.parser")
# print(doc.prettify())

# # version 1
# prices = doc.find_all("p", attrs={"class": "product__price"})
# print(prices[0].string)
# # print(type(prices))

# version 2
prices = doc.find_all("meta", attrs={"id": "twitter:data1"})
print(prices[0].content)
