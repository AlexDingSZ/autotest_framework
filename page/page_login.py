from base.page_base import page_base
from selenium.webdriver.common.by import By
from page.page_pannel import page_pannel


class page_login(page_base):
    user_name = (By.ID,"user_login")
    password=(By.ID,"user_pass")
    btn = (By.ID,"wp-submit")
    error_message=(By.ID,"login_error")

    def __init__(self,driver=None):
        page_base.__init__(self, driver)

    def input_name(self,name):
        self.wait_element(*self.user_name).clear()
        self.wait_element(*self.user_name).send_keys(name)

    def login(self,name,password):
        self.wait_element(*self.user_name).clear()
        self.wait_element(*self.user_name).send_keys(name)
        self.wait_element(*self.password).clear()
        self.wait_element(*self.password).send_keys(password)
        self.wait_element(*self.btn).click()

    def login_pass(self,name,password):
        self.login(name,password)
        return page_pannel(self.driver)

    def login_fail(self,name,password):
        self.login(name, password)
        return  self.wait_element(*self.error_message).text

