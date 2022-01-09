from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# chromeDriverの設定
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--window-size=1920,1080')
chromeOptions.add_argument('--headless')
chromeDriver = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriver, options=chromeOptions)
wait = WebDriverWait(driver=driver, timeout=60)
# ユーザー情報の設定
USERID = ''
PASSWORD = ''

driver.get('https://rakucoin.appspot.com/rakuten/kuji/')
wait.until(EC.presence_of_element_located)
time.sleep(3)
error_flag = False

lotteries = driver.find_elements_by_tag_name('a')

outputs = []

for lottery in lotteries:
    lottery.click()
    wait.until(EC.presence_of_element_located)
    time.sleep(3)
    if error_flag is False:
        try:
            username_input = driver.find_element_by_xpath('//input[@name="u"]')
            print("a")
            username_input.send_keys(USERID)
            time.sleep(1)

            password_input = driver.find_element_by_xpath('//input[@name="p"]')
            password_input.send_keys(PASSWORD)
            time.sleep(1)

            username_input.submit()
            time.sleep(1)

        except Exception:
            error_flg = True
            print('ユーザー名、パスワード入力時にエラーが発生しました。')

    break

driver.close()
driver.quit()

# # shift-jis, utf8, cp932
# with open(f"outputs.csv", "a", newline="", encoding="utf8") as f:
#     writer = csv.writer(f)
#     writer.writerows(outputs)
