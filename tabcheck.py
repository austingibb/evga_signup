from playsound import playsound
from time import sleep
import os
from selenium import webdriver
from sendemail import sendemail
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def tabcheck(url, store, match_condition, soundfile):
    cwd = os.getcwd()
    fp = webdriver.FirefoxProfile(r'C:\Users\austi\AppData\Roaming\Mozilla\Firefox\Profiles\9191asf9.default-release')

    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get(url)
    ahh = False

    soundfile = os.path.join(cwd, soundfile)

    while True:
        if ahh:
            playsound(soundfile)
            sleep(5)
        else:
            sleep(5)
            if match_condition(driver):
                mailbody = """
                    Item is available at {store}
                    {url}
                """.format(url=url, store=store)
                sendemail(body=mailbody)
                ahh = True
            else:
                # playsound(scan_sound)
                print("No sign up found.")
                driver.get(url)
