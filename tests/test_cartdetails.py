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


def test_loginvalid(before_test):
    chrome_driver = webdriver.Chrome(
        "C://Users//swamy//PycharmProjects//automationexample//drivers//chromedriver.exe")
    chrome_driver.get(data['url'])
    chrome_driver.maximize_window()
    title = "My Store"
    assert title == chrome_driver.title
    chrome_driver.find_element_by_partial_link_text("Sign in").click()

    chrome_driver.execute_script("scrollBy(0,250);")

    uname = chrome_driver.find_element_by_id("email")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", uname)
    uname.send_keys(data['username'])

    pwd = chrome_driver.find_element_by_id("passwd")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", pwd)
    pwd.send_keys(data['password'])

    chrome_driver.find_element_by_id("SubmitLogin").click()
    chrome_driver.implicitly_wait(10)

    chrome_driver.find_element_by_id("search_query_top").click()
    chrome_driver.find_element_by_id("search_query_top").clear()
    chrome_driver.find_element_by_id("search_query_top").send_keys("a")
    chrome_driver.implicitly_wait(10)

    chrome_driver.find_element_by_xpath("//body[@id='search']/div[@id='page']/div[@class='columns-container']/div[@id='columns']/div[@class='row']/div[@id='left_column']/div[@id='best-sellers_block_right']/div[@class='block_content']/ul[@class='block_content products-block']/li[1]/a[1]/img[1]").click()
    chrome_driver.implicitly_wait(15)

    addtocart = chrome_driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", addtocart)
    addtocart.click()
    chrome_driver.implicitly_wait(15)

    proceed = chrome_driver.find_element_by_xpath("//span[contains(text(),'Proceed to checkout')]")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", proceed)
    proceed.click()
    chrome_driver.implicitly_wait(15)

    crt = chrome_driver.find_element_by_xpath("//b[contains(text(),'Cart')]")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", crt)
    crt.click()
    chrome_driver.implicitly_wait(15)

    dlt = chrome_driver.find_element_by_xpath("//i[@class='icon-trash']")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", dlt)
    dlt.click()
    chrome_driver.implicitly_wait(15)

    count = chrome_driver.find_element_by_xpath("//span[@class='ajax_cart_no_product']")
    chrome_driver.execute_script("arguments[0].scrollIntoView(true);", count)
    actual_value = count.text
    assert actual_value == "(empty)"

    chrome_driver.find_element_by_link_text("Sign out").click()
    chrome_driver.implicitly_wait(10)

    chrome_driver.close()
    chrome_driver.quit()

