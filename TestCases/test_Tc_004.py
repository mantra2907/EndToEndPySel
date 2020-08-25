from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from  Base import InitiateDriver
import time
def test_fourth():
    driver = InitiateDriver.startBrowser()
    driver.maximize_window()

    #driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("Hello")

    time.sleep(5)
    act=ActionChains(driver)
    #act.click(driver.find_element_by_xpath("//input[@name='fld_username']")).perform()
    act.context_click(driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("abc")).perform()
    InitiateDriver.closeBrowser()