
import unittest


from page.page_login import page_login
from utils.logger import logger
from ddt import ddt,data,unpack

from utils.common import get_parent_path
import os
from utils.readcsv import get_csv_data
logger = logger(logger="test_login").getlog()

@ddt
class test_login(unittest.TestCase):
    test_account = (("admin","123456","admin"),("admin","123456","admin"),("admin","123456","admin"))
    current_path = os.path.dirname(__file__)
    logger.info("__file__ current_path:%s" % current_path)
    test_account = get_csv_data(os.path.join(get_parent_path(current_path),"data","user.csv"))
    logger.info("test_account:%s" % test_account)
    test_account_fail = get_csv_data(os.path.join(get_parent_path(current_path), "data", "user_fail.csv"))
    @classmethod
    def setUpClass(cls):
        cls.p_login = page_login()

    @data(*test_account)
    @unpack
    def test_login_pass(self,name,password,expect_reult):
        self.p_login.driver.get("http://autotest/wordpress/wp-login.php")
        logger.info("start login,acount:%s,password:%s" % (name,password))
        p_pannel = self.p_login.login_pass(name,password)
        actual_result = p_pannel.get_ele_login_name().text
        logger.info("get login name %s" % actual_result)
        logger.info("start checking")
        self.assertEqual(actual_result,expect_reult)
        logger.info("start logout...")
        p_pannel.logout()
        self.p_login.input_name("adfsf")

    @data(*test_account_fail)
    @unpack
    def test_login_fail(self,name,password,expect_reult):
        self.p_login.driver.get("http://autotest/wordpress/wp-login.php")
        logger.info("start login")
        self.p_login.login_fail(name,password)


if __name__ == "__main__":
    unittest.main()
