from utils.HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os

if __name__ == "__main__":
    current_path = os.getcwd()
    root_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    case_path = os.path.join(root_path, "case")
    report_path = os.path.join(root_path, "report")
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.join(report_path,"auto_result_"+now+".html")
    report_file = open(report_path,"wb")

    runner= HTMLTestRunner(stream=report_file,title=u'自动化测试报告',description='执行测试结果')
    cases = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    runner.run(cases)
    report_file.close()

