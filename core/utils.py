from selenium import webdriver
from selenium.webdriver.support.select import Select
import os, time

test_payload = 'autotest'

# 封装了常见的自动化测试的方法，为了统一，只支持开发者使用 xpath 定位目标页面元素
class Utils(object):

    # 初始化页面操作的 webdriver
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    # 根据 xpath 获取标签并点击,并处理弹框
    def get_item_and_click(self, xpath, alert = None):
        tag = self.driver.find_element_by_xpath(xpath)
        href = tag.get_property('href')
         # 记下请求
        if (href) :
            self.logger.info('trigger off the function of %s' % href)
            with open('../logs/urls.log', 'w') as fp:
                fp.write(href)
        
        else :
            self.logger.info('force click')

        try:
            tag.click()
            self.logger.info('The tag was clicked@')
        except Exception as e:
            self.logger.exception('Failed to click the tag with %s' % e)

        # 处理弹出框
        if (alert != None):
            time.sleep(0.5)
            alert_tag = self.driver.switch_to.alert
            try:
                alert_tag.accept()
                self.logger.info('The alert tag was accepted@')
                self.driver.switch_to.default_content()
            except Exception as e:
                self.logger.exception('Failed to accept the alert tag with %s' % e)

    # 根据 xpath 获取标签并向标签发送数据
    def get_item_and_send_keys(self, xpath, keys):

        tag = self.driver.find_element_by_xpath(xpath)
        try:
            tag.send_keys(keys)
            self.logger.info('The keys was sent successfully@')
        except Exception as e:
            self.logger.exception('Failed to send the keys with %s' % e)

    # 选中所有指定索引的下拉框
    def select_all_item(self, index):
        select_tags = self.driver.find_elements_by_tag_name('select')
        try:
            for tag in select_tags:
                s = Select(tag)
                s.select_by_index(index)
            self.logger.info('All the select items were filled@')
        except Exception as e:
            self.logger.exception('Failed to filled all the select items with %s' % e)

    # 根据 xpath 选中下拉框并选中指定索引
    def get_item_and_select(self, xpath, index):
        select_tag = self.driver.find_element_by_xpath(xpath)
        try:
            s = Select(select_tag)
            s.select_by_index(index)
            self.logger.info('select the item as index@')
        except Exception as e:
            self.logger.exception('Failed to select item for index with %s' % e)

    # 根据 id 选中 iframe 并插入测试数据
    def insert_to_iframe(self, id):
        global test_payload
        try:
            self.driver.switch_to.frame(id)
            self.driver.find_element('tag name', 'body').send_keys(test_payload)
            self.driver.switch_to.default_content()
            self.logger.info('insert the data to iframe successfully@')
        except Exception as e:
            self.logger.exception('Failed to filled data to iframe with %s' % e)

    # 向所有文本框插入测试数据
    def insert_to_all_text(self):
        global test_payload
        input_tags = self.driver.find_elements_by_tag_name('input')

        try:
            for tag in input_tags:
                if (tag.get_property('type') == 'text'):
                    tag.send_keys(test_payload)
                else:
                    continue
            self.logger.info('insert the data to all text input items successfully@')
        except Exception as e:
            self.logger.exception('Failed to insert the data to all text input intems with %s' % e)

    # 向 textarea 框中插入测试数据
    def insert_to_all_textarea(self):
        global test_payload
        tags = self.driver.find_elements_by_tag_name('textarea')
        try:
            for tag in tags:
                tag.send_keys(test_payload)
            self.logger.info('insert the data to all textarea items successfully@')
        except Exception as e:
            self.logger.exception('Failed to insert the data to all textarea items with %s' % e)

    # 根据 xpath 选中元素来清除其中内容
    def get_item_and_clear(self, xpath):
        tag = self.driver.find_element_by_xpath(xpath)
        try:
            tag.clear()
            self.logger.info('The %s was clear@' % tag.text)
        except Exception as e:
            self.logger.exception('Failed to clear the text with %s' % e)

    # 登录后台,根据 xpath 定位登录框
    def bg_login(self, username, username_xpath, passwd, passwd_xpath):
        self.get_item_and_send_keys(username_xpath, username)
        self.get_item_and_send_keys(passwd_xpath, passwd)
        self.get_item_and_click('//button[1]')

