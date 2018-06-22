from base.page_base import page_base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class page_pannel(page_base):
    #login_name = (By.XPATH,"//*[@id='wp-admin-bar-my-account']/a/span")
    login_name = (By.XPATH,"//*[@id='wp-admin-bar-my-account']/a/span")
    #logout=(By.XPATH,"//a[.='登出']")
    logout_btn=(By.CSS_SELECTOR,"#wp-admin-bar-logout > a")

    def __init__(self,driver=None):
        page_base.__init__(self,driver)


    def get_ele_login_name(self):
        return self.wait_element(*self.login_name)

    def logout(self):
        log_btn = self.wait_element(*self.login_name)
        ActionChains(self.driver).move_to_element(log_btn).perform()
        self.wait_element(*self.logout_btn).click()

