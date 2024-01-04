from bs4 import BeautifulSoup
import requests
import smtplib

# Email info to connect and send to
EMAIL = "EMAIL_HERE"
PASSWORD = "EMAIL_PASSWORD_HERE"

AMAZON_PRODUCT = "https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68/"
# Headers to properly obtain product price from Amazon
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=AMAZON_PRODUCT, headers=headers)
response.raise_for_status
content = response.text

soup = BeautifulSoup(content, "html.parser")
# Get Product Price as float
product_price = float(soup.find(name="span", class_="a-price-whole").getText().split(".")[0])
# Get product Title
product_title = soup.find(name="span", id="productTitle").get_text()

# Set target price to check and send email with product title, new price and link.
if product_price < 30:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject: Amazon Price Drop Alert!\n\n{product_title} is now ${product_price}\n{AMAZON_PRODUCT}"
    )
else:
    print("Still pricey!")
