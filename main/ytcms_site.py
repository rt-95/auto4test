from autotest.core.utils import Utils
from autotest.core.driver_handler import DriverHandler
import time
import os

class YtSite(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self):
        # 测试网站模块
        self.utils.get_item_and_click('//li[9]/a')
        self.driver.implicitly_wait(3)
        self.utils.get_item_and_click( '//tr[1]//a[2]')
        self.utils.insert_to_all_text()
        self.utils.select_all_item(1)
        self.utils.get_item_and_click('//button[1]')
        self.driver.implicitly_wait(3)