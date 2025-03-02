import time
import requests
from scraper import ScrapeData
from selenium import webdriver
from selenium.webdriver.common.by import By

res = requests.get("https://appbrewery.github.io/Zillow-Clone/")
content = res.text

# configuring browser options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

soup = ScrapeData(content)
soup.get_data()
all_addresses = soup.address_list
all_prices = soup.price_list
all_links = soup.a_list

for i in range(len(all_prices)):

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://forms.gle/m6qiiU48aK7io2Bn7")
    time.sleep(2)

    input_divs = driver.find_elements(By.CSS_SELECTOR, value="input.whsOnd.zHQkBf")
    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    anchor = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address.send_keys(soup.address_list[i])
    price.send_keys(soup.price_list[i])
    anchor.send_keys(soup.a_list[i])

    btn = driver.find_element(By.CSS_SELECTOR, value="span.NPEfkd.RveJvd.snByac")
    btn.click()
    driver.quit()
