from selenium.webdriver.support.select import Select
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest

def datagen():
    li = [['a', 'a@com', '07/29/2000'], ['ab', 'ab@com', '07/29/2001'], ['abc', 'abc@com', '07/29/2002']]
    return li

@pytest.mark.parametrize('data',datagen())
def test_ValidateRegistration(data):
    driver=InitiateDriver.startBrowser()
    Register= RegistrationPage.Registration(driver)
    Register.enter_Username(data[0])
    Register.enter_email(data[1])
    Register.enter_Dob(data[2])
    InitiateDriver.closeBrowser()


