from Library import ConfigReader

class Registration:

    def __init__(self,obj):
        global driver
        driver= obj

    def enter_Username(self, username):
        driver.find_element_by_xpath(ConfigReader.readElementData('Registration', 'user_name')).send_keys(username)

    def enter_email(self,email):
        driver.find_element_by_xpath(ConfigReader.readElementData('Registration', 'email_name')).send_keys(email)

    def enter_Dob(self,DOB):
        driver.find_element_by_xpath(ConfigReader.readElementData('Registration', 'DOB')).send_keys(DOB)