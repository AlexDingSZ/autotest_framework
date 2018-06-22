from selenium import webdriver
import os
from utils.logger import logger
import time

logger = logger(logger="base_page").getlog()
class page_base(object):
    def __init__(self,driver=None):
        if driver is None:
            os.system("taskkill /im chromedriver.exe /f")
            self.driver = webdriver.Chrome()
        else:
            self.driver=driver

    def get_element(self,*locator):
        logger.info("查找元素 %s" % str(locator))
        return self.driver.find_element(*locator)

    def wait_element(self,*locator):
        ele = None
        count = 0
        while ele is None:
            count = count + 1
            try:
                ele = self.driver.find_element(*locator)
            except:
                pass
            flag = ele is not None
            logger.info("第%d次查找元素 %s,查找结果 %s " % (count,str(locator),flag))
            time.sleep(0.1)
            if count > 99:
                logger.info("没有找到元素 %s" % str(locator))
                break
        return ele
