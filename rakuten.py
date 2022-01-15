from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# chromeDriverの設定
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--window-size=1920,1080')
# chromeOptions.add_argument('--headless')
chromeDriver = "chromedriver.exe"
chrome_service = fs.Service(executable_path=chromeDriver)
driver = webdriver.Chrome(service=chrome_service, options=chromeOptions)
wait = WebDriverWait(driver=driver, timeout=60)
# ユーザー情報の設定
USERID = '111420knt@gmail.com'
PASSWORD = '111420knt'

driver.get('https://rakucoin.appspot.com/rakuten/kuji/')
wait.until(EC.presence_of_element_located)
time.sleep(1)

lotteries = driver.find_elements(By.TAG_NAME, 'a')
login_flag = True
outputs = []

for lottery in lotteries:
    lottery.click()
    wait.until(EC.presence_of_element_located)
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])

    if login_flag:
        driver.find_element(By.ID, 'loginInner_u').send_keys(USERID)
        driver.find_element(By.ID, 'loginInner_p').send_keys(PASSWORD)
        driver.find_element(By.CLASS_NAME, 'loginButton').click()
        wait.until(EC.presence_of_element_located)
        time.sleep(3)
        login_flag = False

    if len(driver.find_elements(By.ID, 'entry')) > 0:
        driver.find_element(By.ID, 'entry').click()
        wait.until(EC.presence_of_element_located)
        time.sleep(20)
    #    くじを引くidがentry以外の場合どうするか？

    driver.close()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[0])

driver.close()
driver.quit()
