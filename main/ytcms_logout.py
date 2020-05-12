from autotest.core.utils import Utils
from autotest.core.driver_handler import DriverHandler
import time
import os

class YtLogout(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self):
        # 测试账号模块
        self.utils.get_item_and_click('//li[8]/a')