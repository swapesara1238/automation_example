import json
import os
import pytest
from selenium import webdriver
import sys
import os.path
import time

from selenium.webdriver.support.select import Select

sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def before_test():
    file_path=os.path.sep.join(['config', 'credentials.json']);
    with open(file_path) as json_file:
        global data
        data=json.load(json_file)


def test_registrationvalid(before_test):
    chrome_driver = webdriver.Chrome(
        "C://Users//swamy//PycharmProjects//automationexample//drivers//chromedriver.exe")
    chrome_driver.get(data['url'])
    chrome_driver.maximize_window()
    title = "My Store"
    assert title == chrome_driver.title
    chrome_driver.find_element_by_partial_link_text("Sign in").click()

    chrome_driver.execute_script("scrollBy(0,250);")

    emailcreate = chrome_driver.find_element_by_id("email_create")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", emailcreate)
    emailcreate.send_keys("abc@2.com")
    chrome_driver.find_element_by_id("SubmitCreate").click()
    chrome_driver.implicitly_wait(10)
    chrome_driver.execute_script("window.scrollTo(0, 0);")
    chrome_driver.implicitly_wait(10)

    mrbtn = chrome_driver.find_element_by_xpath("//input[@id='id_gender1']")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", mrbtn)
    mrbtn.click()
    chrome_driver.implicitly_wait(10)
    cfname=chrome_driver.find_element_by_id("customer_firstname")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", cfname)
    cfname.send_keys("abcfname")

    clname = chrome_driver.find_element_by_id("customer_lastname")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", clname)
    clname.send_keys("abclname")

    pwd = chrome_driver.find_element_by_id("passwd")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", pwd)
    pwd.send_keys("abc@123")


    fname = chrome_driver.find_element_by_id("firstname")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", fname)
    fname.send_keys("abcfname")

    lname = chrome_driver.find_element_by_id("lastname")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", lname)
    lname.send_keys("abclname")


    lname = chrome_driver.find_element_by_id("lastname")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", lname)
    lname.send_keys("abclname")

    adr = chrome_driver.find_element_by_id("address1")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", adr)
    adr.send_keys("hyderabad,uppal")
    chrome_driver.find_element_by_id("city").send_keys("Hyderabad")

    selectstate = Select(chrome_driver.find_element_by_id('id_state'))
    selectstate.select_by_visible_text('Alabama')
    chrome_driver.find_element_by_id("postcode").send_keys("14526")

    chrome_driver.implicitly_wait(15)
    mobil = chrome_driver.find_element_by_id("phone_mobile")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", mobil)
    mobil.send_keys("9898989898")

    chrome_driver.find_element_by_id("alias").clear()
    chrome_driver.find_element_by_id("alias").send_keys("Aliasssnmm")
    chrome_driver.find_element_by_xpath("//span[contains(text(),'Register')]").click()
    chrome_driver.implicitly_wait(15)

    welcometext = chrome_driver.find_element_by_xpath("//p[@class='info-account']")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", welcometext)
    actual_value=welcometext.text
    assert actual_value == "Welcome to your account. Here you can manage all of your personal information and orders."

    Signout=chrome_driver.find_element_by_partial_link_text("Sign out")

    chrome_driver.close()
    chrome_driver.quit()

