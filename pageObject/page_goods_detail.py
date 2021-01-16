import allure
from selenium.webdriver.common.by import By

from base.baseApi import Base
import time
import pageObject

class PageGoodsDetail(Base):

    # 点击粉色
    @allure.step('点击粉色')
    def click_pink(self):
        self.base_click(pageObject.loc_pink)

    # 点击M
    @allure.step('点击M')
    def click_M(self):
        self.base_click(pageObject.loc_M)

    # 点击立即购买
    @allure.step('点击立即购买')
    def click_now_buy(self):
        self.base_click(pageObject.loc_now_buy)

    # 加入购物车
    @allure.step('加入购物车')
    def click_add_cart(self):
        self.base_click(pageObject.goods_detail_add_cart)

    @allure.step('点击右上角的购物车')
    def click_right_cart(self):
        self.base_click(pageObject.googs_detail_click_right_cart)











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


