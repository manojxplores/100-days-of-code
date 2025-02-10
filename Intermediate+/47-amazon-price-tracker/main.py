import os
from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import re

PRODUCT_URL = "https://appbrewery.github.io/instant_pot/"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def scrape_data():
    headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    res = requests.get(url=PRODUCT_URL, headers=headers)
    contents = res.text
    soup = BeautifulSoup(contents, "html.parser")

    title = soup.find("span", id="productTitle").getText()
    div = soup.find("div", class_="a-box-group")
    price = div.find("span", class_="a-price-whole").getText()
    total_price = float(re.sub(",", "", price))
    return title, total_price


with SMTP("smtp.gmail.com", port=587) as connection:
    product_title, product_price = scrape_data()
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject: Price drop alert!\n\n{product_title} is now ${product_price}\n{PRODUCT_URL}".strip().encode("UTF-8")
    )
