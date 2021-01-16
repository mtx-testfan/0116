import time

import allure

import pageObject
from base.baseApi import Base
from base.driver import Driver
from pageAction.cart_action import Cart
from pageAction.login_action import Login

'''
case
测试用例（N）
1.起始动作是在哪个页面----
原则：1.保证起始动作在相同的页面---相同的页面就是首页
    2.目的回到首页
    2.1  加入购物车测试用例(前一个测试用例)结束的时候 点击index标签---跳转到首页
    todo： 销毁函数   teardown_method()
    2.2   删除购物车测试用例(后一个测试用例)开始的时候，get(http://121.42.15.146:9090/mtx/)---打开首页
    todo:  初始化函数   setup_method()

'''
@allure.feature('购物车功能的测试')
class TestCart:
    def setup_class(self):
        # 创建driver对象
        self.driver = Driver.get_drvier()
        # 依赖登录,调用成功登录的业务
        Login(self.driver).login_success()
        # 实例化一个Base对象
        self.base = Base(self.driver)
        # 创建Cart对象
        self.cart = Cart(self.driver)

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()

    # # 第一种办法 销毁函数---点击index首页
    # def teardown_method(self):
    #     self.base.base_click_index()
    #第二种方法 初始化函数---get(url)
    def setup_method(self):
        self.driver.get(pageObject.url)

    # 测试用例：添加购物车
    @allure.title('添加购物车的测试用例')
    def test_add(self):
        self.cart.business_add_cart()
        time.sleep(3)
        assert '加入成功' in self.base.base_page_source

    # 删除购物车
    @allure.title('删除购物车的测试用例')
    def test_delete(self):
        self.cart.business_delete_cart()
        time.sleep(3)
        assert "删除成功" in self.base.base_page_source
