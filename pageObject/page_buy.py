import allure
from selenium.webdriver.common.by import By

from base.baseApi import Base
import time
import pageObject

class PageBuy(Base):

    # 点击支付方式
    @allure.step('点击支付方式')
    def click_payment(self):
        self.base_click(pageObject.loc_payment)

    # 点击提交订单
    @allure.step('提交订单')
    def click_submit_order(self):
        self.base_click(pageObject.loc_submit_order)













    # # 组合页面
    # def login_business(self):
    #     # 点击登录链接
    #     self.click_login_link()
    #     # 输入用户名
    #     self.input_username()
    #     # 输入密码
    #     self.input_pwd()
    #     # 点击登录按钮
    #     self.click_login()
    #     time.sleep(2)


