import json
import os
import pandas as pd
import xlwt as xlwt
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

from pdf_read import telebots1

wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Sheet 2')
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
        try:
            image_url = driver.find_element(By.XPATH, '/html/body/div[2]/article[1]/div/div/div[1]/img').get_attribute(
                'src')
            time.sleep(0.65)
            print(image_url)
            folder_path = "C:/Users/ulugbek/PycharmProjects/dtm_uz_parsing/images1"
            filename = os.path.join(folder_path, f"{uni}.jpg")
            urllib.request.urlretrieve(image_url, filename)
            time.sleep(0.4)
        except:
            print('rasm yuklanmadi')
        # kunduzgi_ozbekcha_talim = []
        # kunduzgi_ruscha_talim = []
        # # kunduzgi_inglizcha_talim = []
        # kunduzgi_turkmancha_talim = []
        # kunduzgi_qozoqcha_talim = []
        # kunduzgi_qirgizcha_talim = []
        # kunduzgi_qoraqalpoqcha_talim = []
        # kunduzgi_tojikcha_talim = []
        #
        # sirtqi_ozbekcha_talim = []
        # sirtqi_ruscha_talim = []
        # # sirtqi_inglizcha_talim = []
        # sirtqi_turkmancha_talim = []
        # sirtqi_qozoqcha_talim = []
        # sirtqi_qirgizcha_talim = []
        # sirtqi_qoraqalpoqcha_talim = []
        # sirtqi_tojikcha_talim = []
        #
        # kechki_ozbekcha_talim = []
        # kechki_ruscha_talim = []
        # # kechki_inglizcha_talim = []
        # kechki_turkmancha_talim = []
        # kechki_qozoqcha_talim = []
        # kechki_qirgizcha_talim = []
        # kechki_qoraqalpoqcha_talim = []
        # kechki_tojikcha_talim = []
        #
        # masofaviy_ozbekcha_talim = []
        # masofaviy_ruscha_talim = []
        # # masofaviy_inglizcha_talim = []
        # masofaviy_turkmancha_talim = []
        # masofaviy_qozoqcha_talim = []
        # masofaviy_qirgizcha_talim = []
        # masofaviy_qoraqalpoqcha_talim = []
        # masofaviy_tojikcha_talim = []
        #
        # kunduzgi_uzbekcha_qabul = []
        # kunduzgi_ruscha_qabul = []
        # # kunduzgi_inglizcha_qabul = []
        # kunduzgi_turkmancha_qabul = []
        # kunduzgi_qozoqcha_qabul = []
        # kunduzgi_qirgizcha_qabul = []
        # kunduzgi_qoraqalpoqcha_qabul = []
        # kunduzgi_tojikcha_qabul = []
        #
        # kunduzgi_uzbekcha_grand = []
        # kunduzgi_ruscha_grand = []
        # # kunduzgi_inglizcha_grand = []
        # kunduzgi_turkmancha_grand = []
        # kunduzgi_qozoqcha_grand = []
        # kunduzgi_qirgizcha_grand = []
        # kunduzgi_qoraqalpoqcha_grand = []
        # kunduzgi_tojikcha_grand = []
        #
        # kunduzgi_uzbekcha_kontrakt = []
        # kunduzgi_ruscha_kontrakt = []
        # # kunduzgi_inglizcha_kontrakt = []
        # kunduzgi_turkmancha_kontrakt = []
        # kunduzgi_qozoqcha_kontrakt = []
        # kunduzgi_qirgizcha_kontrakt = []
        # kunduzgi_qoraqalpoqcha_kontrakt = []
        # kunduzgi_tojikcha_kontrakt = []
        #
        # sirtqi_uzbekcha_qabul = []
        # sirtqi_ruscha_qabul = []
        # # sirtqi_inglizcha_qabul = []
        # sirtqi_turkmancha_qabul = []
        # sirtqi_qozoqcha_qabul = []
        # sirtqi_qirgizcha_qabul = []
        # sirtqi_qoraqalpoqcha_qabul = []
        # sirtqi_tojikcha_qabul = []
        #
        # sirtqi_uzbekcha_grand = []
        # sirtqi_ruscha_grand = []
        # # sirtqi_inglizcha_grand = []
        # sirtqi_turkmancha_grand = []
        # sirtqi_qozoqcha_grand = []
        # sirtqi_qirgizcha_grand = []
        # sirtqi_qoraqalpoqcha_grand = []
        # sirtqi_tojikcha_grand = []
        #
        # sirtqi_uzbekcha_kontrakt = []
        # sirtqi_ruscha_kontrakt = []
        # # sirtqi_inglizcha_kontrakt = []
        # sirtqi_turkmancha_kontrakt = []
        # sirtqi_qozoqcha_kontrakt = []
        # sirtqi_qirgizcha_kontrakt = []
        # sirtqi_qoraqalpoqcha_kontrakt = []
        # sirtqi_tojikcha_kontrakt = []
        #
        # kechki_uzbekcha_qabul = []
        # kechki_ruscha_qabul = []
        # # kechki_inglizcha_qabul = []
        # kechki_turkmancha_qabul = []
        # kechki_qozoqcha_qabul = []
        # kechki_qirgizcha_qabul = []
        # kechki_qoraqalpoqcha_qabul = []
        # kechki_tojikcha_qabul = []
        #
        # kechki_uzbekcha_grand = []
        # kechki_ruscha_grand = []
        # # kechki_inglizcha_grand = []
        # kechki_turkmancha_grand = []
        # kechki_qozoqcha_grand = []
        # kechki_qirgizcha_grand = []
        # kechki_qoraqalpoqcha_grand = []
        # kechki_tojikcha_grand = []
        #
        # kechki_uzbekcha_kontrakt = []
        # kechki_ruscha_kontrakt = []
        # # kechki_inglizcha_kontrakt = []
        # kechki_turkmancha_kontrakt = []
        # kechki_qozoqcha_kontrakt = []
        # kechki_qirgizcha_kontrakt = []
        # kechki_qoraqalpoqcha_kontrakt = []
        # kechki_tojikcha_kontrakt = []
        #
        # masofaviy_uzbekcha_qabul = []
        # masofaviy_ruscha_qabul = []
        # # masofaviy_inglizcha_qabul = []
        # masofaviy_turkmancha_qabul = []
        # masofaviy_qozoqcha_qabul = []
        # masofaviy_qirgizcha_qabul = []
        # masofaviy_qoraqalpoqcha_qabul = []
        # masofaviy_tojikcha_qabul = []
        #
        # masofaviy_uzbekcha_grand = []
        # masofaviy_ruscha_grand = []
        # # masofaviy_inglizcha_grand = []
        # masofaviy_turkmancha_grand = []
        # masofaviy_qozoqcha_grand = []
        # masofaviy_qirgizcha_grand = []
        # masofaviy_qoraqalpoqcha_grand = []
        # masofaviy_tojikcha_grand = []
        #
        # masofaviy_uzbekcha_kontrakt = []
        # masofaviy_ruscha_kontrakt = []
        # # masofaviy_inglizcha_kontrakt = []
        # masofaviy_turkmancha_kontrakt = []
        # masofaviy_qozoqcha_kontrakt = []
        # masofaviy_qirgizcha_kontrakt = []
        # masofaviy_qoraqalpoqcha_kontrakt = []
        # masofaviy_tojikcha_kontrakt = []
        #
        # massiv_code = []
        # massiv_nomi = []
        #
        # massiv_kunduzgi = []
        # massiv_sirtqi = []
        # massiv_kechki = []
        # massiv_masofaviy = []
        for k in range(1, 5):
            try:
                talim_shakli = driver.find_element(By.XPATH,
                                                   f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[3]/div/a[{k}]')
                talim_shakli_text = driver.find_element(By.XPATH,
                                                        f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[3]/div/a[{k}]').get_attribute(
                    'textContent')
                talim_shakli.click()
                print(f"\n----{talim_shakli_text}----")
                for i in range(1, 10):
                    try:
                        talim_tili = driver.find_element(By.XPATH,
                                                         f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[{i}]')
                        talim_tili_text = driver.find_element(By.XPATH,
                                                              f'/html/body/div[2]/article[2]/div/div[1]/div[2]/div/div[2]/div/a[{i}]').get_attribute(
                            'textContent')
                        talim_tili.click()
                        print(f"\n----{talim_tili_text}----")
                        t_yonalish = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
                        for yonalish in t_yonalish:
                            try:
                                shtrix_code = yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME, 'div').get_attribute('textContent')
                                time.sleep(1)
                                # print(shtrix_code)
                                # massiv_code.append(shtrix_code)

                                nomi = yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
                                                                                                 'a').text.replace(
                                    shtrix_code, '').strip()
                                # massiv_nomi.append(nomi)
                                # print(nomi)
                                qabul = yonalish.find_elements(By.TAG_NAME, 'td')[1].get_attribute('textContent')
                                grant = yonalish.find_elements(By.TAG_NAME, 'td')[2].get_attribute('textContent')
                                kontarkt = yonalish.find_elements(By.TAG_NAME, 'td')[3].get_attribute('textContent')
                                time.sleep(0.2)
                                print(
                                    f'{nomi}\n{shtrix_code}---------------------------------> {qabul}   {grant}   {kontarkt}')
                                time.sleep(1.2)
                                sheet1.write(count, 1, shtrix_code)
                                sheet1.write(count, 2, nomi)
                                try:
                                    if talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 7, '+')
                                        sheet1.write(count, 35, qabul)
                                        sheet1.write(count, 63, grant)
                                        sheet1.write(count, 91, kontarkt)
                                        # kunduzgi_ozbekcha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_uzbekcha_qabul.append(qabul)
                                        # kunduzgi_uzbekcha_grand.append(grant)
                                        # kunduzgi_uzbekcha_kontrakt.append(kontarkt)
                                except:
                                    print('uzbek kunduzgi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 8, '+')
                                        sheet1.write(count, 36, qabul)
                                        sheet1.write(count, 64, grant)
                                        sheet1.write(count, 92, kontarkt)
                                        # kunduzgi_ruscha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_ruscha_qabul.append(qabul)
                                        # kunduzgi_ruscha_grand.append(grant)
                                        # kunduzgi_ruscha_kontrakt.append(kontarkt)
                                except:
                                    print('rus kunduzgi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 10, '+')
                                        sheet1.write(count, 38, qabul)
                                        sheet1.write(count, 66, grant)
                                        sheet1.write(count, 94, kontarkt)
                                        # kunduzgi_qozoqcha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_qozoqcha_qabul.append(qabul)
                                        # kunduzgi_qozoqcha_grand.append(grant)
                                        # kunduzgi_qozoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qozoq kunduzgi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 11, '+')
                                        sheet1.write(count, 40, qabul)
                                        sheet1.write(count, 68, grant)
                                        sheet1.write(count, 96, kontarkt)
                                        # kunduzgi_qoraqalpoqcha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_qoraqalpoqcha_qabul.append(qabul)
                                        # kunduzgi_qoraqalpoqcha_grand.append(grant)
                                        # kunduzgi_qoraqalpoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qoraqalpoq kunduzgi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 9, '+')
                                        sheet1.write(count, 37, qabul)
                                        sheet1.write(count, 65, grant)
                                        sheet1.write(count, 93, kontarkt)
                                        # kunduzgi_turkmancha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_turkmancha_qabul.append(qabul)
                                        # kunduzgi_turkmancha_grand.append(grant)
                                        # kunduzgi_turkmancha_kontrakt.append(kontarkt)
                                except:
                                    print("turkman kunduzgi yoq")
                                try:
                                    if talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 13, '+')
                                        sheet1.write(count, 41, qabul)
                                        sheet1.write(count, 69, grant)
                                        sheet1.write(count, 97, kontarkt)
                                        # kunduzgi_tojikcha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_tojikcha_qabul.append(qabul)
                                        # kunduzgi_tojikcha_grand.append(grant)
                                        # kunduzgi_tojikcha_kontrakt.append(kontarkt)
                                except:
                                    print("tojik kunduzgi yoq")
                                try:
                                    if talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Kunduzgi':
                                        sheet1.write(count, 3, '+')
                                        sheet1.write(count, 12, '+')
                                        sheet1.write(count, 39, qabul)
                                        sheet1.write(count, 67, grant)
                                        sheet1.write(count, 95, kontarkt)
                                        # kunduzgi_qirgizcha_talim.append('+')
                                        # massiv_kunduzgi.append('+')
                                        # kunduzgi_qirgizcha_qabul.append(qabul)
                                        # kunduzgi_qirgizcha_grand.append(grant)
                                        # kunduzgi_qirgizcha_kontrakt.append(kontarkt)
                                except:
                                    print('qirgiz kunduzgi yoq')
                                try:
                                    if talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 14, '+')
                                        sheet1.write(count, 42, qabul)
                                        sheet1.write(count, 70, grant)
                                        sheet1.write(count, 98, kontarkt)
                                        # sirtqi_ozbekcha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_uzbekcha_qabul.append(qabul)
                                        # sirtqi_uzbekcha_grand.append(grant)
                                        # sirtqi_uzbekcha_kontrakt.append(kontarkt)
                                except:
                                    print('ozbek sirtqi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 15, '+')
                                        sheet1.write(count, 43, qabul)
                                        sheet1.write(count, 71, grant)
                                        sheet1.write(count, 99, kontarkt)
                                        # sirtqi_ruscha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_ruscha_qabul.append(qabul)
                                        # sirtqi_ruscha_grand.append(grant)
                                        # sirtqi_ruscha_kontrakt.append(kontarkt)
                                except:
                                    print('rus sirtqi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 17, '+')
                                        sheet1.write(count, 45, qabul)
                                        sheet1.write(count, 73, grant)
                                        sheet1.write(count, 101, kontarkt)
                                        # sirtqi_qozoqcha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_qozoqcha_qabul.append(qabul)
                                        # sirtqi_qozoqcha_grand.append(grant)
                                        # sirtqi_qozoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qozoq sirtqi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 19, '+')
                                        sheet1.write(count, 47, qabul)
                                        sheet1.write(count, 75, grant)
                                        sheet1.write(count, 103, kontarkt)
                                        # sirtqi_qoraqalpoqcha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_qoraqalpoqcha_qabul.append(qabul)
                                        # sirtqi_qoraqalpoqcha_grand.append(grant)
                                        # sirtqi_qoraqalpoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qoraqalpoq sirtqi')
                                try:
                                    if talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 16, '+')
                                        sheet1.write(count, 44, qabul)
                                        sheet1.write(count, 72, grant)
                                        sheet1.write(count, 107, kontarkt)
                                        # sirtqi_turkmancha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_turkmancha_qabul.append(qabul)
                                        # sirtqi_turkmancha_grand.append(grant)
                                        # sirtqi_turkmancha_kontrakt.append(kontarkt)
                                except:
                                    print('turkman sirtqi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 20, '+')
                                        sheet1.write(count, 48, qabul)
                                        sheet1.write(count, 76, grant)
                                        sheet1.write(count, 104, kontarkt)
                                        # sirtqi_tojikcha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_tojikcha_qabul.append(qabul)
                                        # sirtqi_tojikcha_grand.append(grant)
                                        # sirtqi_tojikcha_kontrakt.append(kontarkt)
                                except:
                                    print('tojik sirtqi yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Sirtqi':
                                        sheet1.write(count, 4, '+')
                                        sheet1.write(count, 18, '+')
                                        sheet1.write(count, 46, qabul)
                                        sheet1.write(count, 74, grant)
                                        sheet1.write(count, 102, kontarkt)
                                        # sirtqi_qirgizcha_talim.append('+')
                                        # massiv_sirtqi.append('+')
                                        # sirtqi_qirgizcha_qabul.append(qabul)
                                        # sirtqi_qirgizcha_grand.append(grant)
                                        # sirtqi_qirgizcha_kontrakt.append(kontarkt)
                                except:
                                    print('qirgiz sirtqi yoq')

                                try:
                                    if talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 21, '+')
                                        sheet1.write(count, 49, qabul)
                                        sheet1.write(count, 77, grant)
                                        sheet1.write(count, 105, kontarkt)
                                        # kechki_ozbekcha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_uzbekcha_qabul.append(qabul)
                                        # kechki_uzbekcha_grand.append(grant)
                                        # kechki_uzbekcha_kontrakt.append(kontarkt)
                                except:
                                    print('ozbek kechki yoq')
                                try:
                                    if talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 22, '+')
                                        sheet1.write(count, 50, qabul)
                                        sheet1.write(count, 78, grant)
                                        sheet1.write(count, 106, kontarkt)
                                        # kechki_ruscha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_ruscha_qabul.append(qabul)
                                        # kechki_ruscha_grand.append(grant)
                                        # kechki_ruscha_kontrakt.append(kontarkt)
                                except:
                                    print('rus kechki')
                                try:
                                    if talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 24, '+')
                                        sheet1.write(count, 52, qabul)
                                        sheet1.write(count, 80, grant)
                                        sheet1.write(count, 108, kontarkt)
                                        # kechki_qozoqcha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_qozoqcha_qabul.append(qabul)
                                        # kechki_qozoqcha_grand.append(grant)
                                        # kechki_qozoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qozoq kechki yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 26, '+')
                                        sheet1.write(count, 54, qabul)
                                        sheet1.write(count, 82, grant)
                                        sheet1.write(count, 104, kontarkt)
                                        # kechki_qoraqalpoqcha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_qoraqalpoqcha_qabul.append(qabul)
                                        # kechki_qoraqalpoqcha_grand.append(grant)
                                        # kechki_qoraqalpoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qoraqalpoq kechki')
                                try:
                                    if talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 23, '+')
                                        sheet1.write(count, 51, qabul)
                                        sheet1.write(count, 79, grant)
                                        sheet1.write(count, 107, kontarkt)
                                        # kechki_turkmancha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_turkmancha_qabul.append(qabul)
                                        # kechki_turkmancha_grand.append(grant)
                                        # kechki_turkmancha_kontrakt.append(kontarkt)
                                except:
                                    print('turkman kechki yoq')
                                try:
                                    if talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 27, '+')
                                        sheet1.write(count, 55, qabul)
                                        sheet1.write(count, 83, grant)
                                        sheet1.write(count, 111, kontarkt)
                                        # kechki_tojikcha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_tojikcha_qabul.append(qabul)
                                        # kechki_tojikcha_grand.append(grant)
                                        # kechki_tojikcha_kontrakt.append(kontarkt)
                                except:
                                    print('tojik kechki yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Kechki':
                                        sheet1.write(count, 5, '+')
                                        sheet1.write(count, 28, '+')
                                        sheet1.write(count, 53, qabul)
                                        sheet1.write(count, 81, grant)
                                        sheet1.write(count, 109, kontarkt)
                                        # kechki_qirgizcha_talim.append('+')
                                        # massiv_kechki.append('+')
                                        # kechki_qirgizcha_qabul.append(qabul)
                                        # kechki_qirgizcha_grand.append(grant)
                                        # kechki_qirgizcha_kontrakt.append(kontarkt)
                                except:
                                    print('qirgiz kechki yoq')

                                try:
                                    if talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 28, '+')
                                        sheet1.write(count, 56, qabul)
                                        sheet1.write(count, 84, grant)
                                        sheet1.write(count, 112, kontarkt)
                                        # masofaviy_ozbekcha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_uzbekcha_qabul.append(qabul)
                                        # masofaviy_uzbekcha_grand.append(grant)
                                        # masofaviy_uzbekcha_kontrakt.append(kontarkt)
                                except:
                                    print('ozbek masofaviy yoq')
                                try:
                                    if talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 29, '+')
                                        sheet1.write(count, 57, qabul)
                                        sheet1.write(count, 85, grant)
                                        sheet1.write(count, 113, kontarkt)
                                        # masofaviy_ruscha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_ruscha_qabul.append(qabul)
                                        # masofaviy_ruscha_grand.append(grant)
                                        # masofaviy_ruscha_kontrakt.append(kontarkt)
                                except:
                                    print('rus masofaviy yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 31, '+')
                                        sheet1.write(count, 52, qabul)
                                        sheet1.write(count, 90, grant)
                                        sheet1.write(count, 115, kontarkt)
                                        # masofaviy_qozoqcha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_qozoqcha_qabul.append(qabul)
                                        # masofaviy_qozoqcha_grand.append(grant)
                                        # masofaviy_qozoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qozoq masofaviy yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 33, '+')
                                        sheet1.write(count, 61, qabul)
                                        sheet1.write(count, 88, grant)
                                        sheet1.write(count, 117, kontarkt)
                                        # masofaviy_qoraqalpoqcha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_qoraqalpoqcha_qabul.append(qabul)
                                        # masofaviy_qoraqalpoqcha_grand.append(grant)
                                        # masofaviy_qoraqalpoqcha_kontrakt.append(kontarkt)
                                except:
                                    print('qoraqalpoq masofaviy yoq')
                                try:
                                    if talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 30, '+')
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 58, qabul)
                                        sheet1.write(count, 86, grant)
                                        sheet1.write(count, 114, kontarkt)
                                        # masofaviy_turkmancha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_turkmancha_qabul.append(qabul)
                                        # masofaviy_turkmancha_grand.append(grant)
                                        # masofaviy_turkmancha_kontrakt.append(kontarkt)
                                except:
                                    print('turkman masofaviy yoq')
                                try:
                                    if talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 34, '+')
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 62, qabul)
                                        sheet1.write(count, 89, grant)
                                        sheet1.write(count, 118, kontarkt)
                                        # masofaviy_tojikcha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_tojikcha_qabul.append(qabul)
                                        # masofaviy_tojikcha_grand.append(grant)
                                        # masofaviy_tojikcha_kontrakt.append(kontarkt)
                                except:
                                    print('tojik masofaviy yoq')
                                try:
                                    if talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Masofaviy':
                                        sheet1.write(count, 32, '+')
                                        sheet1.write(count, 6, '+')
                                        sheet1.write(count, 60, qabul)
                                        sheet1.write(count, 87, grant)
                                        sheet1.write(count, 116, kontarkt)

                                        # masofaviy_qirgizcha_talim.append('+')
                                        # massiv_masofaviy.append('+')
                                        # masofaviy_qirgizcha_qabul.append(qabul)
                                        # masofaviy_qirgizcha_grand.append(grant)
                                        # masofaviy_qirgizcha_kontrakt.append(kontarkt)
                                except:
                                    print('qirgiz masofaviy yoq')

                                # sheet1.write(count, 1, massiv_code)
                                # sheet1.write(count, 2, massiv_nomi)
                                # sheet1.write(count, 3, massiv_kunduzgi)
                                # sheet1.write(count, 4, massiv_sirtqi)
                                # sheet1.write(count, 5, massiv_kechki)
                                # sheet1.write(count, 6, massiv_masofaviy)
                                # sheet1.write(count, 7, kunduzgi_ozbekcha_talim)
                                # sheet1.write(count, 8, kunduzgi_ruscha_talim)
                                # sheet1.write(count, 9, kunduzgi_turkmancha_talim)
                                # sheet1.write(count, 10, kunduzgi_qozoqcha_talim)
                                # sheet1.write(count, 11, kunduzgi_qirgizcha_talim)
                                # sheet1.write(count, 12, kunduzgi_qoraqalpoqcha_talim)
                                # sheet1.write(count, 13, kunduzgi_tojikcha_talim)
                                # sheet1.write(count, 14, kunduzgi_ozbekcha_talim)
                                # sheet1.write(count, 15, kunduzgi_ruscha_talim)
                                # sheet1.write(count, 16, sirtqi_ozbekcha_talim)
                                # sheet1.write(count, 17, sirtqi_ruscha_talim)
                                # sheet1.write(count, 18, sirtqi_turkmancha_talim)
                                # sheet1.write(count, 19, sirtqi_qozoqcha_talim)
                                # sheet1.write(count, 20, sirtqi_qirgizcha_talim)
                                # sheet1.write(count, 21, sirtqi_qoraqalpoqcha_talim)
                                # sheet1.write(count, 22, sirtqi_tojikcha_talim)
                                # sheet1.write(count, 23, kechki_ozbekcha_talim)
                                # sheet1.write(count, 24, kechki_ruscha_talim)
                                # sheet1.write(count, 25, kechki_turkmancha_talim)
                                # sheet1.write(count, 26, kechki_qozoqcha_talim)
                                # sheet1.write(count, 27, kechki_qirgizcha_talim)
                                # sheet1.write(count, 28, kechki_qoraqalpoqcha_talim)
                                # sheet1.write(count, 29, kechki_tojikcha_talim)
                                # sheet1.write(count, 30, masofaviy_ozbekcha_talim)
                                # sheet1.write(count, 31, masofaviy_ruscha_talim)
                                # sheet1.write(count, 32, masofaviy_turkmancha_talim)
                                # sheet1.write(count, 33, masofaviy_qozoqcha_talim)
                                # sheet1.write(count, 34, masofaviy_qirgizcha_talim)
                                # sheet1.write(count, 35, masofaviy_qoraqalpoqcha_talim)
                                # sheet1.write(count, 36, masofaviy_tojikcha_talim)
                                # sheet1.write(count, 37, kunduzgi_uzbekcha_qabul)
                                # sheet1.write(count, 38, kunduzgi_ruscha_talim)
                                # sheet1.write(count, 39, kunduzgi_ruscha_talim)
                                # df = pd.DataFrame({
                                #     'Yo\'nalish kodi': list(massiv_code),
                                #     "Tal'lim yo'nalishi": list(massiv_nomi),
                                #     "Kunduzgi ta'lim": list(massiv_kunduzgi),
                                #     "Sirtqi ta'lim": list(massiv_sirtqi),
                                #     "Kechki ta'lim": list(massiv_kechki),
                                #     "Masofaviy ta'lim": list(massiv_masofaviy),
                                #     "Kunduzgi o'zbek ta'lim": list(kunduzgi_ozbekcha_talim),
                                #     "Kunduzgi rus ta'lim": list(kunduzgi_ruscha_talim),
                                #     "Kunduzgi turkman ta'lim": list(kunduzgi_turkmancha_talim),
                                #     "Kunduzgi qozoq ta'lim": list(kunduzgi_qozoqcha_talim),
                                #     "Kunduzgi qirg'iz ta'lim": list(kunduzgi_qirgizcha_talim),
                                #     "Kunduzgi qoraqalpoq ta'lim": list(kunduzgi_qoraqalpoqcha_talim),
                                #     "Kunduzgi tojik ta'lim": list(kunduzgi_tojikcha_talim),
                                #     "Sirtqi o'zbek ta'lim": list(sirtqi_ozbekcha_talim),
                                #     "Sirtqi rus ta'lim": list(sirtqi_ruscha_talim),
                                #     "Sirtqi turkman ta'lim": list(sirtqi_turkmancha_talim),
                                #     "Sirtqi qozoq ta'lim": list(sirtqi_qozoqcha_talim),
                                #     "Sirtqi qirg'iz ta'lim": list(sirtqi_qirgizcha_talim),
                                #     "Sirtqi qoraqalpoq ta'lim": list(sirtqi_qoraqalpoqcha_talim),
                                #     "Sirtqi tojik ta'lim": list(sirtqi_tojikcha_talim),
                                #     "Kechki o'zbek ta'lim": list(kechki_ozbekcha_talim),
                                #     "Kechki rus ta'lim": list(kechki_ruscha_talim),
                                #     "Kechki turkman ta'lim": list(kechki_turkmancha_talim),
                                #     "Kechki qozoq ta'lim": list(kechki_qozoqcha_talim),
                                #     "Kechki qirg'iz ta'lim": list(kechki_qirgizcha_talim),
                                #     "Kechki qoraqalpoq ta'lim": list(kechki_qoraqalpoqcha_talim),
                                #     "Kechki tojik ta'lim": list(kechki_tojikcha_talim),
                                #     "Masofaviy o'zbek ta'lim": list(masofaviy_ozbekcha_talim),
                                #     "Masofaviy rus ta'lim": list(masofaviy_ruscha_talim),
                                #     "Masofaviy turkman ta'lim": list(masofaviy_turkmancha_talim),
                                #     "Masofaviy qozoq ta'lim": list(masofaviy_qozoqcha_talim),
                                #     "Masofaviy qirg'iz ta'lim": list(masofaviy_qirgizcha_talim),
                                #     "Masofaviy qoraqalpoq ta'lim": list(masofaviy_qoraqalpoqcha_talim),
                                #     "Masofaviy tojik ta'lim": list(masofaviy_tojikcha_talim),
                                #     "Kunduzgi o'zbek qabul": list(kunduzgi_uzbekcha_qabul),
                                #     "Kunduzgi rus qabul": list(kunduzgi_ruscha_qabul),
                                #     "Kunduzgi turkman qabul": list(kunduzgi_turkmancha_qabul),
                                #     "Kunduzgi qozoq qabul": list(kunduzgi_qozoqcha_qabul),
                                #     "Kunduzgi qirg'iz qabul": list(kunduzgi_qirgizcha_qabul),
                                #     "Kunduzgi qoraqalpoq qabul": list(kunduzgi_qoraqalpoqcha_qabul),
                                #     "Kunduzgi tojik qabul": list(kunduzgi_tojikcha_qabul),
                                #     "Sirtqi o'zbek qabul": list(sirtqi_uzbekcha_qabul),
                                #     "Sirtqi rus qabul": list(sirtqi_ruscha_qabul),
                                #     "Sirtqi turkman qabul": list(sirtqi_turkmancha_qabul),
                                #     "Sirtqi qozoq qabul": list(sirtqi_qozoqcha_qabul),
                                #     "Sirtqi qirg'iz qabul": list(sirtqi_qozoqcha_qabul),
                                #     "Sirtqi qoraqalpoq qabul": list(sirtqi_qoraqalpoqcha_qabul),
                                #     "Sirtqi tojik qabul": list(sirtqi_tojikcha_qabul),
                                #     "Kechki o'zbek qabul": list(kechki_uzbekcha_qabul),
                                #     "Kechki rus qabul": list(kechki_ruscha_qabul),
                                #     "Kechki turkman qabul": list(kechki_turkmancha_qabul),
                                #     "Kechki qozoq qabul": list(kechki_qozoqcha_qabul),
                                #     "Kechki qirg'iz qabul": list(kechki_qirgizcha_qabul),
                                #     "Kechki qoraqalpoq qabul": list(kechki_qoraqalpoqcha_qabul),
                                #     "Kechki tojik qabul": list(kechki_tojikcha_qabul),
                                #     "Masofaviy o'zbek qabul": list(masofaviy_uzbekcha_qabul),
                                #     "Masofaviy rus qabul": list(masofaviy_ruscha_qabul),
                                #     "Masofaviy turkman qabul": list(masofaviy_turkmancha_qabul),
                                #     "Masofaviy qozoq qabul": list(masofaviy_qozoqcha_qabul),
                                #     "Masofaviy qirg'iz qabul": list(masofaviy_qirgizcha_qabul),
                                #     "Masofaviy qoraqalpoq qabul": list(masofaviy_qoraqalpoqcha_qabul),
                                #     "Masofaviy tojik qabul": list(masofaviy_tojikcha_qabul),
                                #     "Kunduzgi o'zbek grand": list(kunduzgi_uzbekcha_grand),
                                #     "Kunduzgi rus grand": list(kunduzgi_turkmancha_grand),
                                #     "Kunduzgi turkman grand": list(kunduzgi_turkmancha_grand),
                                #     "Kunduzgi qozoq grand": list(kunduzgi_qozoqcha_grand),
                                #     "Kunduzgi qirg'iz grand": list(kunduzgi_qirgizcha_grand),
                                #     "Kunduzgi qoraqalpoq grand": list(kunduzgi_qoraqalpoqcha_grand),
                                #     "Kunduzgi tojik grand": list(kunduzgi_tojikcha_grand),
                                #     "Sirtqi o'zbek grand": list(sirtqi_uzbekcha_grand),
                                #     "Sirtqi rus grand": list(sirtqi_ruscha_grand),
                                #     "Sirtqi turkman grand": list(sirtqi_turkmancha_grand),
                                #     "Sirtqi qozoq grand": list(sirtqi_qozoqcha_grand),
                                #     "Sirtqi qirg'iz grand": list(sirtqi_qirgizcha_grand),
                                #     "Sirtqi qoraqalpoq grand": list(sirtqi_qoraqalpoqcha_grand),
                                #     "Sirtqi tojik grand": list(sirtqi_tojikcha_grand),
                                #     "Kechki o'zbek grand": list(sirtqi_uzbekcha_grand),
                                #     "Kechki rus grand": list(kechki_ruscha_grand),
                                #     "Kechki turkman grand": list(kechki_turkmancha_grand),
                                #     "Kechki qozoq grand": list(kechki_qozoqcha_grand),
                                #     "Kechki qirg'iz grand": list(kechki_qirgizcha_grand),
                                #     "kechki qoraqalpoq grand": list(kechki_qoraqalpoqcha_grand),
                                #     "Kechki tojik grand": list(kechki_tojikcha_grand),
                                #     "Masofaviy o'zbek grand": list(masofaviy_uzbekcha_grand),
                                #     "Masofaviy rus grand": list(masofaviy_ruscha_grand),
                                #     "Masofaviy turkman grand": list(masofaviy_turkmancha_grand),
                                #     "Masofaviy qirg'iz grand": list(masofaviy_qirgizcha_grand),
                                #     "Masofaviy qoraqalpoq grand": list(masofaviy_qoraqalpoqcha_grand),
                                #     "Masofaviy tojik grand": list(masofaviy_tojikcha_grand),
                                #     "Kunduzgi o'zbek kontrakt": list(kunduzgi_uzbekcha_kontrakt),
                                #     "Kunduzgi rus kontrakt": list(kunduzgi_ruscha_kontrakt),
                                #     "Kunduzgi turkman kontrakt": list(kunduzgi_turkmancha_kontrakt),
                                #     "Kuduzgi qozoq kontrakt": list(kunduzgi_qozoqcha_kontrakt),
                                #     "Kunduzgi qirg'iz kontrakt": list(kunduzgi_qirgizcha_kontrakt),
                                #     "Kunduzgi qoraqalpoq kontrakt": list(kunduzgi_qoraqalpoqcha_kontrakt),
                                #     "Kunduzgi tojik kontrakt": list(kunduzgi_tojikcha_kontrakt),
                                #     "Sirtqi o'zbek kontrakt": list(sirtqi_uzbekcha_kontrakt),
                                #     "Sirtqi rus kontrakt": list(sirtqi_ruscha_kontrakt),
                                #     "Sirtqi turkman kontrakt": list(sirtqi_turkmancha_kontrakt),
                                #     "Sirtqi qozoq kontrakt": list(sirtqi_qozoqcha_kontrakt),
                                #     "Sirtqi qirg'iz kontrakt": list(sirtqi_qirgizcha_kontrakt),
                                #     "Sirtqi qoraqalpoq kontrakt": list(sirtqi_qoraqalpoqcha_kontrakt),
                                #     "Sirtqi tojik kontrakt": list(sirtqi_tojikcha_kontrakt),
                                #     "Kechki o'zbek kontrakt": list(kechki_uzbekcha_kontrakt),
                                #     "Kechki rus kontrakt": list(kechki_ruscha_kontrakt),
                                #     "Kechki turkman kontarkt": list(kechki_turkmancha_kontrakt),
                                #     "Kechki qozoq kontrakt": list(kechki_qozoqcha_kontrakt),
                                #     "Kechki qirg'iz kontrakt": list(kechki_qirgizcha_kontrakt),
                                #     "Kechki qoraqalpoq kontrakt": list(kechki_qoraqalpoqcha_kontrakt),
                                #     "Kechki tojik kontrakt": list(kechki_tojikcha_kontrakt),
                                #     "Masofaviy o'zbek kontrakt": list(masofaviy_uzbekcha_kontrakt),
                                #     "Masofaviy rus kontrakt": list(masofaviy_ruscha_kontrakt),
                                #     "Masofaviy turkman kontrakt": list(masofaviy_turkmancha_kontrakt),
                                #     "Masofaviy qozoq kontrakt": list(masofaviy_qozoqcha_kontrakt),
                                #     "Masofaviy qirg'iz kontrakt": list(masofaviy_qirgizcha_kontrakt),
                                #     "Masofaviy qoraqalpoq kontrakt": list(masofaviy_qoraqalpoqcha_kontrakt),
                                #     "Masofaviy tojik kontrakt": list(masofaviy_tojikcha_kontrakt)
                                #
                                # })
                                # df.to_excel(f'{nomi}.xlsx', index=False)

                            except:
                                print('malumot topilmadi')
                    except:
                        print('Bunday ta\'lim tili mavjud emas')
                        # continue
            except:
                print('---ta\'lim shakli mavjud emas')
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
    telebots1(uni, f'{uni}.xlsx')
    # return f"{uni}.xlsx"


dtm()
