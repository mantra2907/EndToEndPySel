from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Base import InitiateDriver
import time
def test_sixth():
    driver = InitiateDriver.startBrowser()
    driver.maximize_window()

    driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("Hello")

    act=ActionChains(driver)
    # act.send_keys(Keys.TAB).perform()
    #act.key_down(Keys.CONTROL).send_keys('a').perform()
    act.key_down(Keys.CONTROL).send_keys('a').key_down(Keys.CONTROL).send_keys('c').perform()
    time.sleep(5)
    driver.find_element_by_xpath("//input[contains(@placeholder,'myusername@gmail.com')]").send_keys("scenario 5")
    #act.send_keys(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
    #time.sleep(10)
    InitiateDriver.closeBrowser()
