import json
import os

from selenium import webdriver
import selenium.common.exceptions as exc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth
# from selenium_stealth.keyboard import send_keys
import time
import json
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.headless = True
driver = webdriver.Chrome(options=options)

stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

data = []


def dtm():
    driver.get('https://abt.uz/university')
    all_univers = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    for universitet in all_univers:
        uni = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').get_attribute('textContent')
        uni_link = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').get_attribute('href')
        country = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'div').get_attribute(
            'textContent')
        print(uni)
        print(country)
        print(uni_link)
        time.sleep(0.4)
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(uni_link)
        time.sleep(0.2)
        # try:
        #     image_url = driver.find_element(By.XPATH, '/html/body/div[2]/article[1]/div/div/div[1]/img').get_attribute(
        #         'src')
        #     time.sleep(0.65)
        #     print(image_url)
        #     folder_path = "C:/Users/ulugbek/PycharmProjects/dtm_uz_parsing/images1"
        #     filename = os.path.join(folder_path, f"{uni}.jpg")
        #     urllib.request.urlretrieve(image_url, filename)
        #     time.sleep(0.4)
        # except:
        #     print('rasm yuklanmadi')
        # t_yonalish = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        # for yonalish in t_yonalish:
        #     try:
        #
        #         shtrix_code = yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
        #                                                                                 'div').get_attribute(
        #             'textContent')
        #         nomi = yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME, 'a').text.replace(shtrix_code, '').strip()
        #         qabul = yonalish.find_elements(By.TAG_NAME, 'td')[1].get_attribute('textContent')
        #         grant = yonalish.find_elements(By.TAG_NAME, 'td')[2].get_attribute('textContent')
        #         kontarkt = yonalish.find_elements(By.TAG_NAME, 'td')[3].get_attribute('textContent')
        #         time.sleep(0.2)
        #         print(f'{nomi}\n{shtrix_code}---------------------------------> {qabul}   {grant}   {kontarkt}')
        #     except:
        #         print('malumot topilmadi')
        ruscha = driver.find_element(By.XPATH, '/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[2]')
        ruscha.click()


        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # time.sleep(500)
        # data.append(
        #     {'university_name': uni, 'country': country, 'link': uni_link, 'image': f"{folder_path}/{filename}"})
        # time.sleep(0.4)
        # with open('data.json', "w") as f:
        #     json.dump(data, f)

dtm()
