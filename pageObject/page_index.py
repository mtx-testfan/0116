import allure

from base.baseApi import Base
import time
import pageObject
class PageIndex(Base):

    # 在首页点击登录链接
    @allure.step('点击登录链接')
    def click_login_link(self):
        self.base_click(pageObject.index_login_link)

    # 在首页点击zk裙子
    @allure.step('首页-点击zk裙子')
    def click_zk_skirt(self):
        self.base_click(pageObject.loc_zk_skirt)

    # 切换窗口(过渡的动作-前移-写在触发这个动作的页面上)
    @allure.step('切换窗口-从首页到商品详情页')
    def switch_window(self):
        self.base_switch_window(pageObject.title)

        # 点击个人中心
    @allure.step('点击个人中心')
    def click_person_center(self):
        self.base_click(pageObject.index_person_center)

    @allure.step('点击右上角的购物车')
    def click_right_cart(self):
        self.base_click(pageObject.googs_detail_click_right_cart)


