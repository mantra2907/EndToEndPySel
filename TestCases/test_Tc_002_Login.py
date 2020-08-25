import pytest
import openpyxl
from Base import InitiateDriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def test_222():
    '''driver = webdriver.Chrome(executable_path='C:/pychWork/Practise/driver/chromedriver.exe')
    import time
    driver.get("https://www.thetestingworld.com/testings/")'''

    driver = InitiateDriver.startBrowser()
    driver.maximize_window()
    print("Text on link is  :: " +driver.find_element_by_class_name("displayPopup").text)

    print("value of :: "+driver.find_element_by_xpath("//input[@type='submit']").get_attribute("type"))
    InitiateDriver.closeBrowser()



'''
def datagenrator():

    vk=openpyxl.load_workbook("D:/Workspace/EndToEnd/file/TD10.xlsx")
    sh=vk['Sheet1']
    r= sh.max_row
    li=[]
    li1=[]
    for i in range(1, r+1):
        li1=[]
        un=sh.cell[i,1]
        up=sh.cell[i,2]
        #Dob = sh.cell[i,3]
        li1.insert(0,un.value)
        li1.insert(1, up.value)
        li.insert(i-1,li1)
    print(li)
    return li

@pytest.mark.parametrize('data',datagenrator())
def test_ValidateRegistration(data):
    driver=InitiateDriver.startBrowser()
    Register= RegistrationPage.Registration(driver)
    Register.enter_Username(data[0])
    Register.enter_email(data[1])
    Register.enter_Dob(data[2])
    InitiateDriver.closeBrowser()

'''