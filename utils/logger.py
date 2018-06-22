# _*_ coding: utf-8 _*_
import logging
import os.path
import time

class logger(object):
    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '/log/'
        log_name = log_path + rq + '.logs'
        fh = logging.FileHandler(log_name,encoding="utf-8")
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(name)s - line:%(lineno)d')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
    
    

