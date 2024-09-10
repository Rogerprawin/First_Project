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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    try:
        output = float(text.split(": ")[1])
    except (IndexError, ValueError):
        output = float('NaN')  # Handle cases where conversion fails
    return output

def main():
    driver = get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(2)
    
    # Extract text from the web element
    text_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    text = text_element.text  # Get the text from the web element
    
    driver.quit()  # Ensure to quit the driver
    
    # Pass the extracted text to clean_text function
    return clean_text(text)

print(main())
