from selenium import webdriver
from Library import ConfigReader
def startBrowser():
    global driver

    if(ConfigReader.readconfigData('Details','Browser')=="Chrome"):
        path = "./Driver/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)
    elif(ConfigReader.readconfigData('Details','Browser')=="firefox"):
        path="./Driver/geckodriver.exe"
        driver=webdriver.Firefox(executable_path=path)

    #driver.get("https://www.thetestingworld.com/testings/")
    url1=ConfigReader.readconfigData('Details','Application_URL')
    print("url 1 is :: "+url1)
    #driver.get(ConfigReader.readconfigData('Details','Application_URL'))
    driver.get(url1)
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()
