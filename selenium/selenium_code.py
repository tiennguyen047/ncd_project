#!/usr/bin/python3
# copy righter NQT
# tiennguyen047@gmail.com
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(format='%(levelname)s - %(message)s', level="INFO")
url = "https://vnexpress.net/"

def get_driver(url: str):
    options = webdriver.ChromeOptions()
    service = Chrome_Service("/usr/local/share/chromedriver")
    opts = ["disable-infobars", "start-maximized",
            "disable-dev-shm-usage", "no-sandbox", "--headless", "--window-size=1920,1080",
            "--ignore-certificate-errors", "--allow-running-insecure-content", "--disable-gpu"]
    for opt in opts:
        options.add_argument(opt)
    driver = webdriver.Chrome(service=service, options=options, keep_alive=True)
    try:
        time.sleep(2)
        driver.get(url)
    except Exception:
        logging.error("Fail to load url {}".format(url))
    return driver

def get_element(driver: webdriver.Chrome, value: str, by=By.XPATH):
    try:
        element = WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((by, value)))
        return element
    except Exception as e:
        logging.error("Not found element {}".format(e))
        return None

if __name__ == "__main__":
    driver = get_driver(url)
    try:
        element = get_element(driver, "//li[@class='khoahoc']//a[@href='/khoa-hoc']")
        element.click()
        screenshot = driver.save_screenshot('/usr/local/share/test.png')
    finally:
        driver.quit()