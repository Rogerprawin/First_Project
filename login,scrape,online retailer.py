from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="id", value="CustomerEmail").send_keys("roger.prawin1517a@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="CustomerPassword").send_keys("roger.2331387" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click() 
    print(driver.current_url)
print(main())
