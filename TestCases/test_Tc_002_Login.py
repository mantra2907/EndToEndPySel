from selenium.webdriver.support.select import Select
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest
import openpyxl

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