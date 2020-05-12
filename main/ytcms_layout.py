from autotest.core.utils import Utils

import time
import os
# 羊驼cms Page 页面测试类
class YtLayout(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self, xpath):

        # 测试模板，排版，模型模块
        self.utils.get_item_and_click(xpath)
        self.driver.implicitly_wait(3)
        self.utils.get_item_and_click('//div/a')
        self.utils.insert_to_all_text()
        self.utils.insert_to_all_textarea()
        self.utils.get_item_and_click('//button[1]')
        self.driver.implicitly_wait(3)
        self.utils.get_item_and_click('//tr[2]//a[2]', alert = 1)
        self.driver.implicitly_wait(3)

