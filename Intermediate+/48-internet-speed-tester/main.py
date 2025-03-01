from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

start_btn = driver.find_element(By.CLASS_NAME, value="start-text")
start_btn.click()

time.sleep(60)

result_data = driver.find_element(By.CLASS_NAME, value="result-container-data")
up_ele = result_data.find_element(By.CLASS_NAME, value="upload-speed")
down_ele = result_data.find_element(By.CLASS_NAME, value="download-speed")
print(f"down: {down_ele}")
print(f"up: {up_ele}")

driver.quit()
