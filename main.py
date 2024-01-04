from bs4 import BeautifulSoup
import requests

AMAZON_PRODUCT = "https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=AMAZON_PRODUCT, headers=headers)
response.raise_for_status
content = response.text

soup = BeautifulSoup(content, "html.parser")
product_price = float(soup.find(name="span", class_="a-price-whole").getText().split(".")[0])
print(product_price)

if product_price > 50:
    pass
