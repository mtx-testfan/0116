import time

import allure

from base.baseApi import Base
from base.driver import Driver
from pageAction.addaddress_action import AddAddress
from pageAction.login_action import Login
from pageAction.order_action import Order

@allure.feature('新增地址的测试')
class TestAddAddress:
    def setup_class(self):
        # 创建driver对象
        self.driver = Driver.get_drvier()
        # 依赖登录,调用成功登录的业务
        Login(self.driver).login_success()
        # 实例化一个Base对象
        self.base = Base(self.driver)
        # 创建新增地址的对象对象
        self.addaddress = AddAddress(self.driver)

    # 关闭driver
    def teardown_class(self):
        Driver.close_driver()

    # 测试用例：新增地址
    @allure.title('新增地址的正向测试用例')
    def test_add_address(self):
        # 调用增加地址成功的业务
        self.addaddress.addaddress_business()
        # 断言
        time.sleep(1)
        assert '新增成功' in self.base.base_page_source