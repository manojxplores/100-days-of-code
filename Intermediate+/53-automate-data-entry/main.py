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
data_list = [soup.address_list, soup.price_list, soup.a_list]

for i in range(len(soup.address_list)):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://forms.gle/m6qiiU48aK7io2Bn7")
    time.sleep(2)
    input_divs = driver.find_elements(By.CSS_SELECTOR, value="input.whsOnd.zHQkBf")
    for idx, div in enumerate(input_divs):
        div.send_keys(data_list[idx][i])

    btn = driver.find_element(By.CSS_SELECTOR, value="span.NPEfkd.RveJvd.snByac")
    btn.click()
    driver.quit()