from object_repository.RegLoc import Reg_Page_Locators
reg=Reg_Page_Locators()

from time import sleep
class Reg:
    def __init__(self,driver):
        self.driver=driver

    def enter_name(self,a):
        self.driver.find_element(*reg.name).send_keys(a)
        sleep(2)

    def enter_email(self,b):
        self.driver.find_element(*reg.email).send_keys(b)
        sleep(2)

    def enter_pwdd(self,c):
        self.driver.find_element(*reg.pwd).send_keys(c)
        sleep(2)

    def click_regbtn(self):
        self.driver.find_element(*reg.reg_btn).click()
        sleep(2)

