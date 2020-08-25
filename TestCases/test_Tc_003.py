from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Base import InitiateDriver
def test_third():
    driver = InitiateDriver.startBrowser()
    driver.maximize_window()

    print("page title is  :: " +driver.title)
    print("*******************************************")
    print("page URl is :: "+ driver.current_url)

    print("*******************************************")
    print(driver.page_source)
    InitiateDriver.closeBrowser()
