import allure
from selenium.webdriver.common.by import By

from base.baseApi import Base
import time
import pageObject

class PagePersonCenter(Base):

    @allure.step('点击我的地址')
    # 点击我的地址
    def click_my_address(self):
        self.base_click(pageObject.personcenter_myaddress_link)






