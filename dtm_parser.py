import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options,
                          executable_path=r"D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

data = []

array = []
"""
{
    "universitet": "Buxoro davlat universiteti",
    "country": "Buxoro viloyati",
    "education_language": 1,
    "education_type": 1,
    "shtrix_code": "61010313 / Kasbiy (ijodiy) imtihon / Kasbiy (ijodiy) imtihon ",
    "direction_name": "Sport faoliyati: dzyudo\n61010313 / Kasbiy (ijodiy) imtihon / Kasbiy (ijodiy) imtihon",
    "kvota": "2 / 13",
    "grant_ball": "173.6",
    "kontrakt_ball": "72.3"
    
    "direction_id": 117,
    "university_name": "Andijon davlat chet tillari instituti",
    "direction_name": "Filologiya va tillarni o‘qitish: ingliz tili",
    "education_language_id": 1,
    "education_type_id": 1,
    "grant_quota": 10,
    "contract_quota": 15,
    "grant": 174.1,
    "contract": 159.1
    },
"""




def collect_data(uni, country, talim_tili_text, talim_shakli_text, shtrix_code, nomi, qabul, grant, kontrakt):
    talim_tili_mapping = {
        'O‘zbek': 1,
        'Rus': 3,
        'Qozoq': 5,
        'Qoraqalpoq': 6,
        'Turkman': 4,
        'Tojik': 8,
        'Qirg‘iz': 7,
        'Ingliz': 2,
        'Nemis': 11,
        'Arab': 9,
    }

    talim_shakli_mapping = {
        'Kunduzgi': 1,
        'Sirtqi': 2,
        'Kechki': 3,
        'Masofaviy': 4,
    }

    talim_tili_id = talim_tili_mapping.get(talim_tili_text.strip(), None)
    education_type = talim_shakli_mapping.get(talim_shakli_text.strip(), None)

    obj = {
        'universitet': uni,
        'country': country,
        'education_language': talim_tili_id,
        'education_type': education_type,
        'shtrix_code': shtrix_code,
        'direction_name': nomi,
        'kvota': qabul,
        'grant_ball': grant,
        'kontrakt_ball': kontrakt,
    }

    return obj


def modify_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            university_name = i['universitet']
            direction_name = str(i['direction_name']).split('\n')[0]
            education_language = i['education_language']
            education_type = i['education_type']
            grant_quota = int(str(i['kvota']).split('/')[0].strip())
            contract_quota = int(str(i['kvota']).split('/')[1].strip())
            grant = i['grant_ball'] if i.get('grant_ball', None) is not None else None
            contract = i['contract'] if i.get('contract', None) is not None else None
            obj = {
                'university_name': university_name,
                'direction_name': direction_name,
                'education_language_id': education_language,
                "education_type_id": education_type,
                "grant_quota": grant_quota,
                "contract_quota": contract_quota,
                "grant": grant,
                'contract': contract
            }


def dtm():

    driver.get('https://abt.uz/university')
    time.sleep(1)
    all_univers = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    # with open('DATA_23.json', 'r', encoding='utf-8') as f:
    #     data_23 = json.load(f)
    # all_universits = {i['universitet'] for i in data_23}
    for universitet in all_univers:
        try:

            uni = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').text
            time.sleep(0.5)
            print(uni)

            # if uni in all_universits:
            #     continue
            uni_link = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a').get_attribute(
                'href')
            time.sleep(0.2)
            country = universitet.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'div').text
            time.sleep(0.3)
            print(uni)
            print(country)
            print(uni_link)
            time.sleep(0.4)
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(uni_link)
            time.sleep(0.2)
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

                                    nomi = str(
                                        yonalish.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME,
                                                                                                  'a').text)
                                    nomi = str(nomi.replace(shtrix_code, '').strip())
                                    qabul = yonalish.find_elements(By.TAG_NAME, 'td')[1].get_attribute(
                                        'textContent')
                                    grant = yonalish.find_elements(By.TAG_NAME, 'td')[2].get_attribute(
                                        'textContent')
                                    kontrakt = yonalish.find_elements(By.TAG_NAME, 'td')[3].get_attribute(
                                        'textContent')
                                    time.sleep(1.2)
                                    print(
                                        f'{nomi}\n{shtrix_code}---------------------------------> {qabul}   {grant}  {kontrakt}\n')
                                    # data_obj = check_and_append(uni, country, talim_tili_text, talim_shakli_text, shtrix_code,
                                    #                  nomi, qabul, grant, kontrakt)

                                    # time.sleep(1.2)

                                    try:
                                        if talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Kunduzgi':
                                            print(talim_tili_text, 'talim tili')
                                            print('\n----ozbekcha kunduzgi---\n')
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Kunduzgi':
                                            print(talim_tili_text, 'talim tili')
                                            print('\n---ruscha kunduzgi ---\n')
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')


                                        elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Kunduzgi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Kunduzgi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Kunduzgi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Kunduzgi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Kunduzgi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Sirtqi':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Kechki':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == "O‘zbek" and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Rus' and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qozoq' and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qoraqalpoq' and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Turkman' and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Tojik' and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')

                                        elif talim_tili_text.strip() == 'Qirg‘iz' and talim_shakli_text.strip() == 'Masofaviy':
                                            data_obj = collect_data(uni, country, talim_tili_text,
                                                                    talim_shakli_text,
                                                                    shtrix_code, nomi, qabul, grant, kontrakt)
                                            print(json.dumps(data_obj, indent=4, ensure_ascii=False))
                                            array.append(data_obj)
                                            with open("original_2023_quota.json", "a", encoding='utf-8') as f:
                                                json.dump(data_obj, f, indent=4, ensure_ascii=False)
                                                f.write(',')
                                                f.write('\n')
                                        else:
                                            print('data yoq')
                                    except Exception as e:
                                        print('malumot topilmadi', e)
                                except Exception as e:
                                    print('malumot topilmadi', e)

                        except:
                            print('Bunday ta\'lim tili mavjud emas')
                            continue
                except:
                    print('---ta\'lim shakli mavjud emas')
                    continue
        except:
            print('uni , uni_link topilmadi')
            continue
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    return array


dtm()
jsons = dtm()
with open("DATA1_23-1.json", 'w', encoding='utf-8') as f:
    json.dump(jsons, f, indent=4, ensure_ascii=False)
