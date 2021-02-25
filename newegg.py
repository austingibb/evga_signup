import os, time
from multiprocessing import Process
import tabcheck

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

urls = [
    "https://www.newegg.com/black-montech-sky-atx-mid-tower/p/2AM-00CN-00015?Item=9SIAK91C2U6212&Description=3080&cm_re=3080-_-9SIAK91C2U6212-_-Product&cm_sp=SP-_-448371-_-0-_-1-_-9SIAK91C2U6212-_-3080-_-3080-_-13",
    # "https://www.bestbuy.com/site/pny-nvidia-geforce-rtx-3060-12gb-xlr8-gaming-revel-epic-x-rgb-dual-fan-graphics-card/6454319.p?skuId=6454319",
    # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454328.p?skuId=6454328",
    # "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ventus-3x-12g-oc-12gb-gddr6-pci-express-4-0-graphics-card-black/6452940.p?skuId=6452940",
    # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444449.p?skuId=6444449",
]


def found_condition(driver):
    elem = driver.find_elements(By.ID, 'ProductBuy')
    if len(elem) > 0:
        cart_button = elem[0].text
        print(cart_button)
        if "cart" in cart_button.lower():
            return True

    return False

if __name__ == "__main__":
    procs = []

    for url in urls:
        p = Process(target=tabcheck.tabcheck, args=(url, "new egg", found_condition, "newegg.wav"))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()



