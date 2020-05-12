from autotest.core.utils import Utils
from autotest.core.driver_handler import DriverHandler
import time
import os

class YtProfile(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self):

        # 测试账号模块
        self.utils.get_item_and_click('//li[7]/a')
        self.driver.implicitly_wait(3)
        self.utils.get_item_and_send_keys('//form/div[3]/div/input', 'admin')
        self.utils.get_item_and_send_keys('//form/div[4]/div/input', 'admin')
        self.utils.get_item_and_click( '//button')
        self.driver.back()
        self.utils.bg_login('admin', '//form/div[2]/div/input', 'admin', '//form/div[3]/div/input')
        self.utils.get_item_and_click('//tbody/tr[1]//a[1]')
