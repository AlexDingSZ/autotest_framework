import unittest
import time
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from utils.HTMLTestRunner import HTMLTestRunner
from utils.logger import logger

logger = logger(logger="test_login").getlog()

if __name__ == "__main__":
    logger.info("start run test")
    logger.info("root_path:%s" % root_path)
    case_path = os.path.join(root_path, "case")
    report_path = os.path.join(root_path, "report")
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    current_path = os.getcwd()
    root_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

    report_path = os.path.join(report_path,"auto_result_"+now+".html")
    logger.info(report_path)
    report_file = open(report_path,"wb")
    logger.info("report_path:%s" % report_file)

    runner= HTMLTestRunner(stream=report_file,title=u'自动化测试报告',description='执行测试结果')
    cases = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    runner.run(cases)
    report_file.close()

