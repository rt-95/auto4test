import os
from selenium import webdriver
from configparser import ConfigParser
from core.logger import Logger



class DriverHandler(object):

    # 根据配置文件配置初始化 webdriver
    def init_driver(self, log_name):
        # 读入配置文件
        config_handler = ConfigParser()
        path = os.path.dirname(os.path.abspath('.')) + '/config.ini'
        config_handler.read(path)

        # 获取日志记录器
        self.logger = Logger(logger=log_name).get_logger()

        # 获取配置文件属性
        browser_name = config_handler.get('BrowserType', 'BrowserName')
        self.logger.info('You have choose the %s browser to driver.' % browser_name)
        self.url = config_handler.get('TestDomain', 'URL')
        self.logger.info('The testing Domain is %s' % self.url)
        exe_file = config_handler.get('WebDriver', 'Path')
        quiet_mode = config_handler.get('QuietMode', 'value')

        if browser_name == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser_name == 'Chrome':
            # 谷歌浏览器是否启用静默模式
            if (int(quiet_mode) == 1):
                options = webdriver.ChromeOptions()
                options.add_argument('headless')
                self.driver = webdriver.Chrome(options=options)
            else:
                self.driver = webdriver.Chrome(exe_file)
        elif browser_name == 'IE':
            self.driver = webdriver.Ie(exe_file)

        return self.driver

    # 关闭并退出浏览器
    def close_driver(self):
        self.logger.info('It\'s time to close the webdriver')
        self.driver.quit()
