import allure
from selenium.webdriver.common.by import By

from base.baseApi import Base
import time
import pageObject

class PageMyAddress(Base):

    # 输入用户名
    @allure.step('点击新增地址的按钮')
    def click_new_address(self):
        self.base_click(pageObject.myaddress_add_address)

    #   通过index  从0开始  目标iframe是index=2第三个iframe
    @allure.step('切换iframe-编辑我的新地址页面')
    def switch_to_iframe(self):
        # 通过iframe的索引值进行定位
        # self.driver.switch_to.frame(2)
        self.base_switch_iframe(2)

    #
    @allure.step('输入用户名')
    def input_name(self):

        self.base_input(pageObject.myaddress_username,'zuocheng')
    # 输入电话
    @allure.step('输入电话')
    def input_tel(self):
        self.base_input(pageObject.myaddress_tel,'13636751740')

    @allure.step('选择省份')
    def select_prov(self):
        # js-select 显示
        self.base_js(pageObject.myaddress_js_prov)
        # select 省  选择北京
        self.base_select_visible_text(pageObject.myaddress_prov,'北京市')
        time.sleep(2)

    @allure.step('选择城市')
    def select_city(self):
        self.base_js(pageObject.myaddress_js_city)
        # select 省  选择北京
        self.base_select_visible_text(pageObject.myaddress_city, '西城区')
        time.sleep(2)

    @allure.step('选择区县')
    def select_country(self):
        self.base_js(pageObject.myaddress_js_country)
        # select 省  选择北京
        self.base_select_visible_text(pageObject.myaddress_country, '月坛街道')
        time.sleep(2)

    # 详细地址
    @allure.step('输入详细地址')
    def input_detail_address(self):
        self.base_input(pageObject.myaddress_detailaddress,'北京市西城区')

    # 别名
    @allure.step('输入别名')
    def address_nickname(self):
        self.base_input(pageObject.myaddress_nickname,'0113')


    # 点击保存
    @allure.step('点击保存')
    def address_save(self):
        self.base_click(pageObject.myaddress_save)


