import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://kwf.ytit.uz/#individual_overall_289')
# OE8l6KRDw
d = driver.find_element(By.NAME, 'kerio_password')
d.send_keys("OE8l6KRDw")
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
time.sleep(3)
while True:
    driver.refresh()
    time.sleep(180)
