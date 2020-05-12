import logging
import os.path
import time

class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_name = logger

        # 创建一个 handler，用于收集触发功能的 href, 以触发时间作为文件名
        file_name = self.log_name
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_path = log_path + file_name + '.log'

        # 创建文件写入 handler
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.INFO)

        # 再创建一个 handler， 用于输出信息到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义输出格式
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(format)
        ch.setFormatter(format)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    # 获取到 logger
    def get_logger(self):
        return self.logger
