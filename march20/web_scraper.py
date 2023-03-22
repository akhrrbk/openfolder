# this is a web scraper that extracts the price from olcha.uz website
# built by github.com/akhrrbk

from bs4 import BeautifulSoup
import requests
import re
import json

urls = [
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-128gb-deep-purple",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-256gb-deep-purple",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-512-gb-deep-purple",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-1-tb-deep-purple",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-128gb-space-black",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-256gb-space-black",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-512-gb-space-black",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-space-black-1-tb",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-128gb-silver",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-256gb-silver",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-512-gb-silver",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-silver-1-tb",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-128gb-gold",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-256gb-gold",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-512-gb-gold",
            "name": "",
            "price": ""
        },
        {
            "url": "https://olcha.uz/oz/product/view/apple-iphone-14-pro-gold-1-tb",
            "name": "",
            "price": ""
        }
    ]

for i in range(len(urls)):

    # print(urls[i]["url"])
    
    results = requests.get(urls[i]["url"])

    doc = BeautifulSoup(results.text, "html.parser")
    # print(doc.prettify())

    # version 1 - finds the line where the price is located 
    prices = doc.find_all("p", attrs={"class": "product__price"})
    # print(prices[0].string)
    # print(type(prices))

    productinfo = doc.find_all("h1", attrs={"id": "product-title"})
    urls[i]["name"] = productinfo[0].string.strip()
    # print("name: " + urls[i]["name"])

    # function that extacts the price from a string
    def extract_numbers(s):
        pattern = r'\d+'
        numbers = re.findall(pattern, s)
        return ','.join(numbers)

    s = prices[0].string
    urls[i]["price"] = extract_numbers(s)
    # print("price: " + urls[i]["name"])
    
for i in range(len(urls)):
    print(str(i) + ": " + urls[i]["name"] + " - " + urls[i]["price"] + " so'm ")

# nameinput = input('Please choose any of the above(1-4): ')
# nameinput = int(nameinput) - 1

# print("\nname: " + urls[nameinput]["name"])
# print("price: " + urls[nameinput]["price"])
# print("link: " + urls[nameinput]["url"])

# turning the list into JSON
# jsonurls = json.dumps(urls)