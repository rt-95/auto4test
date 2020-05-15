import sys
sys.path.append('../')
from core.utils import Utils
from core.driver_handler import DriverHandler
import time
import os
# 羊驼cms Page 页面测试类
class YtPage(object):

    def __init__(self, driver, logger, url):
        self.driver = driver
        self.logger = logger
        self.url = url
        self.utils = Utils(self.driver, self.logger)

    def run(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
        self.utils.bg_login('admin', '//form/div[2]/div/input', 'admin', '//form/div[3]/div/input')
        self.driver.implicitly_wait(3)
        self.utils.get_item_and_click('//tbody/tr[1]//a[1]')
        # 等待加载页面
        self.driver.implicitly_wait(3)
        # 添加页面
        self.utils.get_item_and_click('//div[@class="pull-right"]/a')
        self.driver.implicitly_wait(3)
        # 文本框插入测试数据
        self.utils.insert_to_all_text()
        # iframe 标签插入测试数据
        self.utils.insert_to_iframe('content_ifr')
        # 选择框插入测试数据
        self.utils.select_all_item(1)
        # 数字文本框插入选择数据
        self.utils.get_item_and_send_keys('//input[@type="number"]', 99)
        # 保存操作
        self.utils.get_item_and_click('//button[@value="save"]')
        self.driver.implicitly_wait(3)
        # 上传测试文件
        self.utils.get_item_and_send_keys('//input[@type="file"]', os.path.dirname(os.path.abspath('.')) + '/data/img/95.jpg')
        # 提交所有操作
        self.utils.get_item_and_click('//form/div[1]/div[1]/button[1]')
        self.driver.implicitly_wait(3)
        # 测试删除功能
        self.utils.get_item_and_click('//tbody/tr[1]/td[6]/a[3]', alert = 1)

