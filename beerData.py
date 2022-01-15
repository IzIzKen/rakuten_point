from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# chromeDriverの設定
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--window-size=1920,1080')
chromeOptions.add_argument('--headless')
chromeDriver = "chromedriver.exe"
chrome_service = fs.Service(executable_path=chromeDriver)
driver = webdriver.Chrome(service=chrome_service, options=chromeOptions)
wait = WebDriverWait(driver=driver, timeout=60)

# 次のページへの画像src属性の値
next_page_src = "http://www.beer365.net/images/pagernext_red.png"

driver.get('http://www.beer365.net/rankings/')
wait.until(EC.presence_of_element_located)
time.sleep(1)

id = 1
outputs = ['id', 'name', 'img_src', 'evaluation', 'looks', 'smell', 'taste', 'throat', 'total', 'style', 'ABV', 'IBU', 'brewery', 'description']
beer_images = []

pages = driver.find_element(By.CLASS_NAME, 'pager').find_elements(By.TAG_NAME, 'span')

for page in pages:
    i = 1
    beer_names = driver.find_element(By.TAG_NAME, 'table').find_elements(By.TAG_NAME, 'a')
    for beer_name in beer_names:
        beer_names_in_loop = driver.find_element(By.TAG_NAME, 'table').find_elements(By.TAG_NAME, 'a')
        beer_names_in_loop[i - 1].click()
        wait.until(EC.presence_of_element_located)
        time.sleep(1)
        name = driver.find_element(By.CLASS_NAME, 'detail').text
        img = driver.find_element(By.XPATH, '//*[@id="mainlowcol"]/div[2]/div/div[1]/p/img')
        img_src = img.get_attribute("src")
        ratebox = driver.find_element(By.CLASS_NAME, 'ratebox')
        evaluation = ratebox.find_elements(By.TAG_NAME, 'span')[0].text
        looks = ratebox.find_elements(By.TAG_NAME, 'span')[1].text
        smell = ratebox.find_elements(By.TAG_NAME, 'span')[2].text
        taste = ratebox.find_elements(By.TAG_NAME, 'span')[3].text
        throat = ratebox.find_elements(By.TAG_NAME, 'span')[4].text
        total = ratebox.find_elements(By.TAG_NAME, 'span')[5].text
        table = driver.find_element(By.TAG_NAME, 'table')
        style = driver.find_elements(By.TAG_NAME, 'td')[0].text
        ABV = driver.find_elements(By.TAG_NAME, 'td')[1].text
        IBU = driver.find_elements(By.TAG_NAME, 'td')[2].text
        brewery = driver.find_elements(By.TAG_NAME, 'td')[3].text
        description = driver.find_element(By.CLASS_NAME, 'mb20').text
        row = [id, name, img_src, evaluation, looks, smell, taste, throat, total, style, ABV, IBU, brewery, description]
        outputs.append(row)
        png = img.screenshot_as_png
        img_name = name + '.png'
        with open(name + '.png', "wb") as f:
            f.write(png)
        print(id, name, img_src, evaluation, looks, smell, taste, throat, total, style, ABV, IBU, brewery, description)
        i += 1
        id += 1
        driver.back()
        wait.until(EC.presence_of_element_located)
        time.sleep(1)
        break
    pager = driver.find_element(By.CLASS_NAME, 'pager')
    page_btns = pager.find_elements(By.TAG_NAME, 'a')
    page_btns[-1].click()
    break

driver.close()
driver.quit()

# shift-jis, utf8, cp932
# with open(f"beersDatabase.csv", "w", newline="", encoding="utf8") as f:
#     writer = csv.writer(f)
#     writer.writerows(outputs)
# for beer_image in beer_images:
#     png = beer_image.screenshot_as_png
#     with open('beerImages', "wb") as f:
#         f.write(png)
