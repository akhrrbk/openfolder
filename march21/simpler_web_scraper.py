import requests
from bs4 import BeautifulSoup

url = "https://olcha.uz/oz/product/view/apple-iphone-14-pro"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# find the name of the product
name = soup.find("h1", {"class": "product-name"}).text.strip()

# find the available colors
colors = []
color_options = soup.find("div", {"class": "options-color"})
if color_options:
    for option in color_options.find_all("div", {"class": "option"}):
        color = option.get("data-title")
        if color:
            colors.append(color)

# find the price
price = soup.find("span", {"class": "price-new"}).text.strip()

print("Name: ", name)
print("Colors: ", colors)
print("Price: ", price)
