import allure
from selenium.webdriver.common.by import By

from base.baseApi import Base
import time
import pageObject

class PageLogin(Base):

    # 输入用户名
    @allure.step('输入用户名')
    def input_username(self,username):
        # 找到用户名的按钮，点击输入

        self.base_input(pageObject.login_name,username)
    # 输入密码
    @allure.step('输入密码')
    def input_pwd(self,password):

        self.base_input(pageObject.login_pwd,password)
    # 点击登录
    @allure.step('点击登录')
    def click_login_button(self):
        self.base_click(pageObject.login_button)















