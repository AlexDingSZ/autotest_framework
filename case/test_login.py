import unittest
from page.page_login import page_login
from utils.logger import logger
from ddt import ddt,data,unpack

logger = logger(logger="test_login").getlog()

@ddt
class test_login(unittest.TestCase):
    test_account = (("admin","123456","admin"),("admin","123456","admin"),("admin","123456","admin"))
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
        logger("start logout...")
        p_pannel.logout()


if __name__ == "__main__":
    unittest.main()