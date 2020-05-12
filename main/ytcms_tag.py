from autotest.core.utils import Utils
from autotest.core.driver_handler import DriverHandler
import time
import os
# 羊驼cms Page 页面测试类
class YtTag(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self):

        # 测试标签模块
        self.utils.get_item_and_click('//li[3]/a')
        self.driver.implicitly_wait(3)
        self.utils.insert_to_all_text()
        self.utils.insert_to_all_textarea()
        self.utils.get_item_and_click('//button[1]')
        self.driver.implicitly_wait(3)

