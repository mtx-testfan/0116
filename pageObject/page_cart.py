import allure
from selenium.webdriver.common.by import By

from base.baseApi import Base
import time
import pageObject

class PageCart(Base):


    @allure.step('点击删除按钮')
    def click_delete_button(self):
        self.base_click(pageObject.cart_delete_button)

    #确定删除
    @allure.step('确定删除')
    def click_confirm_delete(self):
        self.base_click(pageObject.cart_confirm_delete)


