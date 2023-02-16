import datetime

import pandas as pd
import requests

# massiv_code = ['1', 'ds', 's']
# massiv_nomi = ['sds', 'sdsd', 'sd']
# massiv_kunduzgi = ['eer', 'erere', 's']
# create a sample dataframe
# df = pd.DataFrame({
#     'AA': [1, 2, 3],
#     'BB': [4, 5, 6],
#     'CC': [7, 8, 9],
# })

# write the dataframe to an excel file
# df.to_excel('example5.xlsx', index=False)


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAFeaNW1dtleNNM4DDPBnvpC7XdtTZ687mo/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


def telebots1(mess, file_path):
    now = datetime.datetime.now()
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Telegram API endpoint for sending documents
    endpoint = "https://api.telegram.org/bot2090467761:AAHh3xty_m8W7TuiIGs_49zUUJM22pLUdbk/sendDocument"

    # Define the chat ID and message text
    chat_id = "-1001816056115"
    message = {"chat_id": chat_id, "caption": mess, "parse_mode": "HTML"}

    # Read the file content and add it to the request
    with open(file_path, "rb") as f:
        files = {"document": f}
        response = requests.post(endpoint, data=message, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        # telebots('Message and file sent successfully!')
        print("Message and file sent successfully!")
    else:
        # telebots(f"Failed to send message and file. Response: {response.text}")
        print(f"Failed to send message and file. Response: {response.text}")

    # telebots1(files, file_origin)
