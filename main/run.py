from autotest.main.ytcms_page import YtPage
from autotest.main.ytcms_link import YtLink
from autotest.main.ytcms_tag import YtTag
from autotest.main.ytcms_layout import YtLayout
from autotest.main.ytcms_profile import YtProfile
from autotest.main.ytcms_site import YtSite
from autotest.main.ytcms_logout import YtLogout
from autotest.core.driver_handler import DriverHandler
import time

if __name__ == '__main__':
    driver_handler = DriverHandler()
    driver = driver_handler.init_driver('yt_test')
    logger = driver_handler.logger
    url = driver_handler.url
    page = YtPage(driver, logger, url)
    page.run()
    link = YtLink(driver, logger, url)
    link.run()
    tag = YtTag(driver, logger, url)
    tag.run()
    layout = YtLayout(driver, logger, url)
    for i in range(4, 7):
        layout.run('//li[%d]/a' % i)
    profile = YtProfile(driver, logger, url)
    profile.run()
    site = YtSite(driver, logger, url)
    site.run()
    logout = YtLogout(driver, logger, url)
    logout.run()
    driver.quit()