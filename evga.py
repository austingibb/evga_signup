import os
import tabcheck
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

urls = [
    "https://www.evga.com/products/autoNotify.aspx?pn=12G-P5-3657-KR"
]

def found_condition(driver):
    elem = driver.find_elements(By.ID, 'tbFirstName')
    if len(elem) > 0:
        product_text = driver.find_elements(By.TAG_NAME, 'h1')
        product_text = product_text[0].text
        print("product text:", product_text)
        return True

    return False

tabcheck.tabcheck(urls[0], "evga", found_condition, "evga.wav")
