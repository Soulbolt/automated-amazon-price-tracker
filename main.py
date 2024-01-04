from bs4 import BeautifulSoup
import requests

AMAZON_PRODUCT = "https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68/"

response = requests.get(url=AMAZON_PRODUCT)
response.raise_for_status
content = response.text

soup = BeautifulSoup(content, "html.parser")
print(soup)
