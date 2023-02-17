import os

import openpyxl
import pandas as pd
import xlwt as xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import urllib.request

from pdf_read import telebots1

wb = xlwt.Workbook()

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

sheet1 = wb.add_sheet(f'sheet 1')
# sheet1.write(0, 0, 'Universitet nomi')
sheet1.write(0, 1, 'Yo\'nalish kodi')
sheet1.write(0, 2, "Tal'lim yo'nalishi")
sheet1.write(0, 3, "Kunduzgi ta'lim")
sheet1.write(0, 4, "Sirtqi ta'lim")
sheet1.write(0, 5, "Kechki ta'lim")
sheet1.write(0, 6, "Masofaviy ta'lim")
sheet1.write(0, 7, "Kunduzgi o'zbek ta'lim")
sheet1.write(0, 8, "Kunduzgi rus ta'lim")
sheet1.write(0, 9, "Kunduzgi turkman ta'lim")
sheet1.write(0, 10, "Kunduzgi qozoq ta'lim")
sheet1.write(0, 11, "Kunduzgi qoraqalpoq ta'lim")
sheet1.write(0, 12, "Kunduzgi qirg'iz ta'lim")
sheet1.write(0, 13, "Kunduzgi tojik ta'lim")
sheet1.write(0, 14, "Sirtqi o'zbek ta'lim")
sheet1.write(0, 15, "Sirtqi rus ta'lim")
sheet1.write(0, 16, "Sirtqi turkman ta'lim")
sheet1.write(0, 17, "Sirtqi qozoq ta'lim")
sheet1.write(0, 18, "Sirtqi qirg'iz ta'lim")
sheet1.write(0, 19, "Sirtqi qoraqalpoq ta'lim")
sheet1.write(0, 20, "Sirtqi tojik ta'lim")
sheet1.write(0, 21, "Kechki o'zbek ta'lim")
sheet1.write(0, 22, "Kechki rus ta'lim")
sheet1.write(0, 23, "Kechki turkman ta'lim")
sheet1.write(0, 24, "Kechki qozoq ta'lim")
sheet1.write(0, 25, "Kechki qirg'iz ta'lim")
sheet1.write(0, 26, "Kechki qoraqalpoq ta'lim")
sheet1.write(0, 27, "Kechki tojik ta'lim")
sheet1.write(0, 28, "Masofaviy o'zbek ta'lim")
sheet1.write(0, 29, "Masofaviy rus ta'lim")
sheet1.write(0, 30, "Masofaviy turkman ta'lim")
sheet1.write(0, 31, "Masofaviy qozoq ta'lim")
sheet1.write(0, 32, "Masofaviy qirg'iz ta'lim")
sheet1.write(0, 33, "Masofaviy qoraqalpoq ta'lim")
sheet1.write(0, 34, "Masofaviy tojik ta'lim")
sheet1.write(0, 35, "Kunduzgi o'zbek qabul")
sheet1.write(0, 36, "Kunduzgi rus qabul")
sheet1.write(0, 37, "Kunduzgi turkman qabul")
sheet1.write(0, 38, "Kunduzgi qozoq qabul")
sheet1.write(0, 39, "Kunduzgi qirg'iz qabul")
sheet1.write(0, 40, "Kunduzgi qoraqalpoq qabul")
sheet1.write(0, 41, "Kunduzgi tojik qabul")
sheet1.write(0, 42, "Sirtqi o'zbek qabul")
sheet1.write(0, 43, "Sirtqi rus qabul")
sheet1.write(0, 44, "Sirtqi turkman qabul")
sheet1.write(0, 45, "Sirtqi qozoq qabul")
sheet1.write(0, 46, "Sirtqi qirg'iz qabul")
sheet1.write(0, 47, "Sirtqi qoraqalpoq qabul")
sheet1.write(0, 48, "Sirtqi tojik qabul")
sheet1.write(0, 49, "Kechki o'zbek qabul")
sheet1.write(0, 50, "Kechki rus qabul")
sheet1.write(0, 51, "Kechki turkman qabul")
sheet1.write(0, 52, "Kechki qozoq qabul")
sheet1.write(0, 53, "Kechki qirg'iz qabul")
sheet1.write(0, 54, "Kechki qoraqalpoq qabul")
sheet1.write(0, 55, "Kechki tojik qabul")
sheet1.write(0, 56, "Masofaviy o'zbek qabul")
sheet1.write(0, 57, "Masofaviy rus qabul")
sheet1.write(0, 58, "Masofaviy turkman qabul")
sheet1.write(0, 59, "Masofaviy qozoq qabul")
sheet1.write(0, 60, "Masofaviy qirg'iz qabul")
sheet1.write(0, 61, "Masofaviy qoraqalpoq qabul")
sheet1.write(0, 62, "Masofaviy tojik qabul")
sheet1.write(0, 63, "Kunduzgi o'zbek grand")
sheet1.write(0, 64, "Kunduzgi rus grand")
sheet1.write(0, 65, "Kunduzgi turkman grand")
sheet1.write(0, 66, "Kunduzgi qozoq grand")
sheet1.write(0, 67, "Kunduzgi qirg'iz grand")
sheet1.write(0, 68, "Kunduzgi qoraqalpoq grand")
sheet1.write(0, 69, "Kunduzgi tojik grand")
sheet1.write(0, 70, "Sirtqi o'zbek grand")
sheet1.write(0, 71, "Sirtqi rus grand")
sheet1.write(0, 72, "Sirtqi turkman grand")
sheet1.write(0, 73, "Sirtqi qozoq grand")
sheet1.write(0, 74, "Sirtqi qirg'iz grand")
sheet1.write(0, 75, "Sirtqi qoraqalpoq grand")
sheet1.write(0, 76, "Sirtqi tojik grand")
sheet1.write(0, 77, "Kechki o'zbek grand")
sheet1.write(0, 78, "Kechki rus grand")
sheet1.write(0, 79, "Kechki turkman grand")
sheet1.write(0, 80, "Kechki qozoq grand")
sheet1.write(0, 81, "Kechki qirg'iz grand")
sheet1.write(0, 82, "kechki qoraqalpoq grand")
sheet1.write(0, 83, "Kechki tojik grand")
sheet1.write(0, 84, "Masofaviy o'zbek grand")
sheet1.write(0, 85, "Masofaviy rus grand")
sheet1.write(0, 86, "Masofaviy turkman grand")
sheet1.write(0, 87, "Masofaviy qirg'iz grand")
sheet1.write(0, 88, "Masofaviy qoraqalpoq grand")
sheet1.write(0, 89, "Masofaviy tojik grand")
sheet1.write(0, 90, "Masofaviy qozoq grand")
sheet1.write(0, 91, "Kunduzgi o'zbek kontrakt")
sheet1.write(0, 92, "Kunduzgi rus kontrakt")
sheet1.write(0, 93, "Kunduzgi turkman kontrakt")
sheet1.write(0, 94, "Kuduzgi qozoq kontrakt")
sheet1.write(0, 95, "Kunduzgi qirg'iz kontrakt")
sheet1.write(0, 96, "Kunduzgi qoraqalpoq kontrakt")
sheet1.write(0, 97, "Kunduzgi tojik kontrakt")
sheet1.write(0, 98, "Sirtqi o'zbek kontrakt")
sheet1.write(0, 99, "Sirtqi rus kontrakt")
sheet1.write(0, 100, "Sirtqi turkman kontrakt")
sheet1.write(0, 101, "Sirtqi qozoq kontrakt")
sheet1.write(0, 102, "Sirtqi qirg'iz kontrakt")
sheet1.write(0, 103, "Sirtqi qoraqalpoq kontrakt")
sheet1.write(0, 104, "Sirtqi tojik kontrakt")
sheet1.write(0, 105, "Kechki o'zbek kontrakt")
sheet1.write(0, 106, "Kechki rus kontrakt")
sheet1.write(0, 107, "Kechki turkman kontarkt")
sheet1.write(0, 108, "Kechki qozoq kontrakt")
sheet1.write(0, 109, "Kechki qirg'iz kontrakt")
sheet1.write(0, 110, "Kechki qoraqalpoq kontrakt")
sheet1.write(0, 111, "Kechki tojik kontrakt")
sheet1.write(0, 112, "Masofaviy o'zbek kontrakt")
sheet1.write(0, 113, "Masofaviy rus kontrakt")
sheet1.write(0, 114, "Masofaviy turkman kontrakt")
sheet1.write(0, 115, "Masofaviy qozoq kontrakt")
sheet1.write(0, 116, "Masofaviy qirg'iz kontrakt")
sheet1.write(0, 117, "Masofaviy qoraqalpoq kontrakt")
sheet1.write(0, 118, "Masofaviy tojik kontrakt")


def dtm():
    driver.get('https://abt.uz/university')
    all_univers = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    count = 1
    for universitet in all_univers:
        try:

            uni = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').text
            time.sleep(1.5)
            print(uni)
            #sheet1.write(count, 0, kontarkt)


            uni_link = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').get_attribute('href')
            country = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'div').text
            print(uni)
            print(country)
            print(uni_link)
            time.sleep(0.4)
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(uni_link)
            time.sleep(0.2)
            try:
                image_url = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/article[1]/div/div/div[1]/img').get_attribute(
                    'src')
                time.sleep(0.65)
                print(image_url)
                folder_path = "C:/Users/ulugbek/PycharmProjects/dtm_uz_parsing/images1"
                filename = os.path.join(folder_path, f"{uni}.jpg")
                urllib.request.urlretrieve(image_url, filename)
                time.sleep(0.4)
            except Exception as e:
                print('rasm yuklanmadi', e)
            for k in range(1, 5):
                try:
                    talim_shakli = driver.find_element(By.XPATH,
                                                       f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[3]/div/a[{k}]')
                    talim_shakli_text = driver.find_element(By.XPATH,
                                                            f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[3]/div/a[{k}]') \
                        .get_attribute('textContent')
                    talim_shakli.click()
                    print(f"\n----{talim_shakli_text}----")
                    for i in range(1, 8):
                        try:
                            talim_tili = driver.find_element(By.XPATH,
                                                             f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[{i}]')
                            talim_tili_text = driver.find_element(By.XPATH,
                                                                  f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[{i}]').text
                            talim_tili.click()
                            print(f"\n----{talim_tili_text}----")
                            t_yonalish = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

                            for yonalish in t_yonalish:
                                try:
                                    time.sleep(3)
                                    shtrix_code = str(
                                        yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
                                                                                                  'div').get_attribute(
                                            'textContent'))
                                    time.sleep(1)
                                    # print(shtrix_code)
                                    # massiv_code.append(shtrix_code)

                                    nomi = str(
                                        yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
                                                                                                  'a').text)
                                    nomi = str(nomi.replace(shtrix_code, '').strip())
                                    # time.sleep(1.2)
                                    # massiv_nomi.append(nomi)
                                    # print(nomi)
                                    qabul = yonalish.find_elements(By.TAG_NAME, 'td')[1].get_attribute('textContent')
                                    grant = yonalish.find_elements(By.TAG_NAME, 'td')[2].get_attribute('textContent')
                                    kontarkt = yonalish.find_elements(By.TAG_NAME, 'td')[3].get_attribute('textContent')
                                    time.sleep(1.2)
                                    print(
                                        f'{nomi}\n{shtrix_code}---------------------------------> {qabul}   {grant}  {kontarkt}\n')
                                    # time.sleep(1.2)

                                    # try:
                                    if talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Kunduzgi':
                                        print(talim_tili_text, 'talim tili')
                                        print('\n----ozbekcha kunduzgi---\n')
                                        print(count, 'count')
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 7, '+')
                                        sheet1.write(count, 35, qabul)
                                        sheet1.write(count, 63, grant)
                                        sheet1.write(count, 91, kontarkt)
                                        count += 1

                                    elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Kunduzgi':
                                        print(talim_tili_text, 'talim tili')
                                        print('\n---ruscha kunduzgi ---\n')
                                        print(count, 'count')
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 8, '+')
                                        sheet1.write(count, 36, qabul)
                                        sheet1.write(count, 64, grant)
                                        sheet1.write(count, 92, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('uzbek kunduzgi yoq', e)
                                    # try:

                                    # except Exception as e:
                                    #     print('rus kunduzgi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 10, '+')
                                        sheet1.write(count, 38, qabul)
                                        sheet1.write(count, 66, grant)
                                        sheet1.write(count, 94, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qozoq kunduzgi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 11, '+')
                                        sheet1.write(count, 40, qabul)
                                        sheet1.write(count, 68, grant)
                                        sheet1.write(count, 96, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qoraqalpoq kunduzgi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 9, '+')
                                        sheet1.write(count, 37, qabul)
                                        sheet1.write(count, 65, grant)
                                        sheet1.write(count, 93, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print("turkman kunduzgi yoq", e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 13, '+')
                                        sheet1.write(count, 41, qabul)
                                        sheet1.write(count, 69, grant)
                                        sheet1.write(count, 97, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print("tojik kunduzgi yoq", e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 12, '+')
                                        sheet1.write(count, 39, qabul)
                                        sheet1.write(count, 67, grant)
                                        sheet1.write(count, 95, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qirgiz kunduzgi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 14, '+')
                                        sheet1.write(count, 42, qabul)
                                        sheet1.write(count, 70, grant)
                                        sheet1.write(count, 98, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('ozbek sirtqi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 15, '+')
                                        sheet1.write(count, 43, qabul)
                                        sheet1.write(count, 71, grant)
                                        sheet1.write(count, 99, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('rus sirtqi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 17, '+')
                                        sheet1.write(count, 45, qabul)
                                        sheet1.write(count, 73, grant)
                                        sheet1.write(count, 101, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qozoq sirtqi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 19, '+')
                                        sheet1.write(count, 47, qabul)
                                        sheet1.write(count, 75, grant)
                                        sheet1.write(count, 103, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qoraqalpoq sirtqi', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 16, '+')
                                        sheet1.write(count, 44, qabul)
                                        sheet1.write(count, 72, grant)
                                        sheet1.write(count, 107, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('turkman sirtqi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 20, '+')
                                        sheet1.write(count, 48, qabul)
                                        sheet1.write(count, 76, grant)
                                        sheet1.write(count, 104, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('tojik sirtqi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 18, '+')
                                        sheet1.write(count, 46, qabul)
                                        sheet1.write(count, 74, grant)
                                        sheet1.write(count, 102, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qirgiz sirtqi yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 21, '+')
                                        sheet1.write(count, 49, qabul)
                                        sheet1.write(count, 77, grant)
                                        sheet1.write(count, 105, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('ozbek kechki yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 22, '+')
                                        sheet1.write(count, 50, qabul)
                                        sheet1.write(count, 78, grant)
                                        sheet1.write(count, 106, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('rus kechki', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 24, '+')
                                        sheet1.write(count, 52, qabul)
                                        sheet1.write(count, 80, grant)
                                        sheet1.write(count, 108, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qozoq kechki yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 26, '+')
                                        sheet1.write(count, 54, qabul)
                                        sheet1.write(count, 82, grant)
                                        sheet1.write(count, 104, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qoraqalpoq kechki', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 23, '+')
                                        sheet1.write(count, 51, qabul)
                                        sheet1.write(count, 79, grant)
                                        sheet1.write(count, 107, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('turkman kechki yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 27, '+')
                                        sheet1.write(count, 55, qabul)
                                        sheet1.write(count, 83, grant)
                                        sheet1.write(count, 111, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('tojik kechki yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 28, '+')
                                        sheet1.write(count, 53, qabul)
                                        sheet1.write(count, 81, grant)
                                        sheet1.write(count, 109, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qirgiz kechki yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 28, '+')
                                        sheet1.write(count, 56, qabul)
                                        sheet1.write(count, 84, grant)
                                        sheet1.write(count, 112, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('ozbek masofaviy yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 29, '+')
                                        sheet1.write(count, 57, qabul)
                                        sheet1.write(count, 85, grant)
                                        sheet1.write(count, 113, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('rus masofaviy yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 31, '+')
                                        sheet1.write(count, 52, qabul)
                                        sheet1.write(count, 90, grant)
                                        sheet1.write(count, 115, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qozoq masofaviy yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 33, '+')
                                        sheet1.write(count, 61, qabul)
                                        sheet1.write(count, 88, grant)
                                        sheet1.write(count, 117, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qoraqalpoq masofaviy yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 30, '+')
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 58, qabul)
                                        sheet1.write(count, 86, grant)
                                        sheet1.write(count, 114, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('turkman masofaviy yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 34, '+')
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 62, qabul)
                                        sheet1.write(count, 89, grant)
                                        sheet1.write(count, 118, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('tojik masofaviy yoq', e)
                                    # try:
                                    elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 1, shtrix_code)
                                        sheet1.write(count, 2, nomi)
                                        sheet1.write(count, 32, '+')
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 60, qabul)
                                        sheet1.write(count, 87, grant)
                                        sheet1.write(count, 116, kontarkt)
                                        count += 1
                                    # except Exception as e:
                                    #     print('qirgiz masofaviy yoq', e)
                                    else:
                                        print('data yoq')
                                except Exception as e:
                                    print('malumot topilmadi', e)

                        except:
                            print('Bunday ta\'lim tili mavjud emas')
                            continue
                            # time.sleep(0.7)
                except:
                    print('---ta\'lim shakli mavjud emas')
                    continue
                    # time.sleep(0.8)
        except:
            print('uni , uni_link topilmadi')

        # print(kunduzgi_uzbekcha_kontrakt)
        # print(kunduzgi_uzbekcha_qabul)
        # print(kunduzgi_uzbekcha_grand)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # time.sleep(500)
        # data.append(
        #     {'university_name': uni, 'country': country, 'link': uni_link, 'image': f"{folder_path}/{filename}"})
        # time.sleep(0.4)
        # with open('data.json', "w") as f:
        #     json.dump(data, f)
        wb.save(f'{uni}.xls')
        df = pd.read_excel(f"{uni}.xls")
        df.to_excel(f"{uni}.xlsx", index=False)
        df = pd.read_excel(f'{uni}.xlsx')
        df = df.dropna(axis=1, how='all')
        df.to_excel(f'{uni}.xlsx', index=False)
        telebots1(uni, f'{uni}.xlsx')
        count += 1
    return f"{uni}.xlsx"


# try:
#     sheets = 1
#     while True:
#         sheet1 = wb.add_sheet(f'sheet{sheets}')
#         sheet1.write(0, 1, 'Yo\'nalish kodi')
#         sheet1.write(0, 2, "Tal'lim yo'nalishi")
#         sheet1.write(0, 3, "Kunduzgi ta'lim")
#         sheet1.write(0, 4, "Sirtqi ta'lim")
#         sheet1.write(0, 5, "Kechki ta'lim")
#         sheet1.write(0, 6, "Masofaviy ta'lim")
#         sheet1.write(0, 7, "Kunduzgi o'zbek ta'lim")
#         sheet1.write(0, 8, "Kunduzgi rus ta'lim")
#         sheet1.write(0, 9, "Kunduzgi turkman ta'lim")
#         sheet1.write(0, 10, "Kunduzgi qozoq ta'lim")
#         sheet1.write(0, 11, "Kunduzgi qoraqalpoq ta'lim")
#         sheet1.write(0, 12, "Kunduzgi qirg'iz ta'lim")
#         sheet1.write(0, 13, "Kunduzgi tojik ta'lim")
#         sheet1.write(0, 14, "Sirtqi o'zbek ta'lim")
#         sheet1.write(0, 15, "Sirtqi rus ta'lim")
#         sheet1.write(0, 16, "Sirtqi turkman ta'lim")
#         sheet1.write(0, 17, "Sirtqi qozoq ta'lim")
#         sheet1.write(0, 18, "Sirtqi qirg'iz ta'lim")
#         sheet1.write(0, 19, "Sirtqi qoraqalpoq ta'lim")
#         sheet1.write(0, 20, "Sirtqi tojik ta'lim")
#         sheet1.write(0, 21, "Kechki o'zbek ta'lim")
#         sheet1.write(0, 22, "Kechki rus ta'lim")
#         sheet1.write(0, 23, "Kechki turkman ta'lim")
#         sheet1.write(0, 24, "Kechki qozoq ta'lim")
#         sheet1.write(0, 25, "Kechki qirg'iz ta'lim")
#         sheet1.write(0, 26, "Kechki qoraqalpoq ta'lim")
#         sheet1.write(0, 27, "Kechki tojik ta'lim")
#         sheet1.write(0, 28, "Masofaviy o'zbek ta'lim")
#         sheet1.write(0, 29, "Masofaviy rus ta'lim")
#         sheet1.write(0, 30, "Masofaviy turkman ta'lim")
#         sheet1.write(0, 31, "Masofaviy qozoq ta'lim")
#         sheet1.write(0, 32, "Masofaviy qirg'iz ta'lim")
#         sheet1.write(0, 33, "Masofaviy qoraqalpoq ta'lim")
#         sheet1.write(0, 34, "Masofaviy tojik ta'lim")
#         sheet1.write(0, 35, "Kunduzgi o'zbek qabul")
#         sheet1.write(0, 36, "Kunduzgi rus qabul")
#         sheet1.write(0, 37, "Kunduzgi turkman qabul")
#         sheet1.write(0, 38, "Kunduzgi qozoq qabul")
#         sheet1.write(0, 39, "Kunduzgi qirg'iz qabul")
#         sheet1.write(0, 40, "Kunduzgi qoraqalpoq qabul")
#         sheet1.write(0, 41, "Kunduzgi tojik qabul")
#         sheet1.write(0, 42, "Sirtqi o'zbek qabul")
#         sheet1.write(0, 43, "Sirtqi rus qabul")
#         sheet1.write(0, 44, "Sirtqi turkman qabul")
#         sheet1.write(0, 45, "Sirtqi qozoq qabul")
#         sheet1.write(0, 46, "Sirtqi qirg'iz qabul")
#         sheet1.write(0, 47, "Sirtqi qoraqalpoq qabul")
#         sheet1.write(0, 48, "Sirtqi tojik qabul")
#         sheet1.write(0, 49, "Kechki o'zbek qabul")
#         sheet1.write(0, 50, "Kechki rus qabul")
#         sheet1.write(0, 51, "Kechki turkman qabul")
#         sheet1.write(0, 52, "Kechki qozoq qabul")
#         sheet1.write(0, 53, "Kechki qirg'iz qabul")
#         sheet1.write(0, 54, "Kechki qoraqalpoq qabul")
#         sheet1.write(0, 55, "Kechki tojik qabul")
#         sheet1.write(0, 56, "Masofaviy o'zbek qabul")
#         sheet1.write(0, 57, "Masofaviy rus qabul")
#         sheet1.write(0, 58, "Masofaviy turkman qabul")
#         sheet1.write(0, 59, "Masofaviy qozoq qabul")
#         sheet1.write(0, 60, "Masofaviy qirg'iz qabul")
#         sheet1.write(0, 61, "Masofaviy qoraqalpoq qabul")
#         sheet1.write(0, 62, "Masofaviy tojik qabul")
#         sheet1.write(0, 63, "Kunduzgi o'zbek grand")
#         sheet1.write(0, 64, "Kunduzgi rus grand")
#         sheet1.write(0, 65, "Kunduzgi turkman grand")
#         sheet1.write(0, 66, "Kunduzgi qozoq grand")
#         sheet1.write(0, 67, "Kunduzgi qirg'iz grand")
#         sheet1.write(0, 68, "Kunduzgi qoraqalpoq grand")
#         sheet1.write(0, 69, "Kunduzgi tojik grand")
#         sheet1.write(0, 70, "Sirtqi o'zbek grand")
#         sheet1.write(0, 71, "Sirtqi rus grand")
#         sheet1.write(0, 72, "Sirtqi turkman grand")
#         sheet1.write(0, 73, "Sirtqi qozoq grand")
#         sheet1.write(0, 74, "Sirtqi qirg'iz grand")
#         sheet1.write(0, 75, "Sirtqi qoraqalpoq grand")
#         sheet1.write(0, 76, "Sirtqi tojik grand")
#         sheet1.write(0, 77, "Kechki o'zbek grand")
#         sheet1.write(0, 78, "Kechki rus grand")
#         sheet1.write(0, 79, "Kechki turkman grand")
#         sheet1.write(0, 80, "Kechki qozoq grand")
#         sheet1.write(0, 81, "Kechki qirg'iz grand")
#         sheet1.write(0, 82, "kechki qoraqalpoq grand")
#         sheet1.write(0, 83, "Kechki tojik grand")
#         sheet1.write(0, 84, "Masofaviy o'zbek grand")
#         sheet1.write(0, 85, "Masofaviy rus grand")
#         sheet1.write(0, 86, "Masofaviy turkman grand")
#         sheet1.write(0, 87, "Masofaviy qirg'iz grand")
#         sheet1.write(0, 88, "Masofaviy qoraqalpoq grand")
#         sheet1.write(0, 89, "Masofaviy tojik grand")
#         sheet1.write(0, 90, "Masofaviy qozoq grand")
#         sheet1.write(0, 91, "Kunduzgi o'zbek kontrakt")
#         sheet1.write(0, 92, "Kunduzgi rus kontrakt")
#         sheet1.write(0, 93, "Kunduzgi turkman kontrakt")
#         sheet1.write(0, 94, "Kuduzgi qozoq kontrakt")
#         sheet1.write(0, 95, "Kunduzgi qirg'iz kontrakt")
#         sheet1.write(0, 96, "Kunduzgi qoraqalpoq kontrakt")
#         sheet1.write(0, 97, "Kunduzgi tojik kontrakt")
#         sheet1.write(0, 98, "Sirtqi o'zbek kontrakt")
#         sheet1.write(0, 99, "Sirtqi rus kontrakt")
#         sheet1.write(0, 100, "Sirtqi turkman kontrakt")
#         sheet1.write(0, 101, "Sirtqi qozoq kontrakt")
#         sheet1.write(0, 102, "Sirtqi qirg'iz kontrakt")
#         sheet1.write(0, 103, "Sirtqi qoraqalpoq kontrakt")
#         sheet1.write(0, 104, "Sirtqi tojik kontrakt")
#         sheet1.write(0, 105, "Kechki o'zbek kontrakt")
#         sheet1.write(0, 106, "Kechki rus kontrakt")
#         sheet1.write(0, 107, "Kechki turkman kontarkt")
#         sheet1.write(0, 108, "Kechki qozoq kontrakt")
#         sheet1.write(0, 109, "Kechki qirg'iz kontrakt")
#         sheet1.write(0, 110, "Kechki qoraqalpoq kontrakt")
#         sheet1.write(0, 111, "Kechki tojik kontrakt")
#         sheet1.write(0, 112, "Masofaviy o'zbek kontrakt")
#         sheet1.write(0, 113, "Masofaviy rus kontrakt")
#         sheet1.write(0, 114, "Masofaviy turkman kontrakt")
#         sheet1.write(0, 115, "Masofaviy qozoq kontrakt")
#         sheet1.write(0, 116, "Masofaviy qirg'iz kontrakt")
#         sheet1.write(0, 117, "Masofaviy qoraqalpoq kontrakt")
#         sheet1.write(0, 118, "Masofaviy tojik kontrakt")
#         sheets += 1
#         dtm()
#
# except:
#     print('OTM tugadi')
dtm()
