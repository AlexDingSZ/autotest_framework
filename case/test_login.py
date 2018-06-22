import unittest
from page.page_login import page_login
from utils.logger import logger
from ddt import ddt,data,unpack
from utils.readcsv import get_csv_data
from utils.common import get_parent_path
import os
logger = logger(logger="test_login").getlog()

@ddt
class test_login(unittest.TestCase):
    test_account = (("admin","123456","admin"),("admin","123456","admin"),("admin","123456","admin"))
    test_account = get_csv_data(os.path.join(get_parent_path(os.getcwd()),"data","user.csv"))
    @classmethod
    def setUpClass(cls):
        cls.p_login = page_login()

    @data(*test_account)
    @unpack
    def test_login_pass(self,name,password,expect_reult):
        self.p_login.driver.get("http://autotest/wordpress/wp-login.php")
        logger.info("start login")
        p_pannel = self.p_login.login("admin","123456")
        actual_result = p_pannel.get_ele_login_name().text
        logger.info("get login name %s" % actual_result)
        logger.info("start checking")
        self.assertEqual(actual_result,expect_reult)
        logger.info("start logout...")
        p_pannel.logout()


if __name__ == "__main__":
    unittest.main()
