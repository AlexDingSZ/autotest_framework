
import unittest
import time
import os
import sys
sys.path.append(r"D:\pycode\autotest_framework\base")
sys.path.append(r"D:\pycode\autotest_framework\case")
sys.path.append(r"D:\pycode\autotest_framework\base")
sys.path.append(r"D:\pycode\autotest_framework\page")
sys.path.append(r"D:\pycode\autotest_framework\utils")
sys.path.append(r"D:\pycode\autotest_framework\log")
sys.path.append(r"D:\pycode\autotest_framework\report")
sys.path.append(r"D:\pycode\autotest_framework")
from utils.HTMLTestRunner import HTMLTestRunner
from utils.logger import logger

logger = logger(logger="test_login").getlog()
if __name__ == "__main__":
    logger.info("start run test")
    current_file_path = os.path.dirname(__file__)
    root_path = os.path.abspath(os.path.dirname(current_file_path) + os.path.sep + ".")
    case_path = os.path.join(root_path, "case")
    report_path = os.path.join(root_path, "report")
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.join(report_path,"auto_result_"+now+".html")
    logger.info(report_path)
    report_file = open(report_path,"wb")
    logger.info("report_path:%s" % report_file)

    runner= HTMLTestRunner(stream=report_file,title=u'自动化测试报告',description='执行测试结果')
    cases = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    runner.run(cases)
    report_file.close()

