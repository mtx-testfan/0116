import time

import pytest

from base.driver import Driver
from pageAction.login_action import Login
from tool.readData import ReadData
from base.baseApi import Base
data = ReadData().get_yaml('login_data','test_login')
'''
登录用例的参数化数据如何组织？如何断言
1.前面是登录失败的，后面一条是登录成功的(推荐写法)，前提条件：setup_class,teardown_class
2.没有顺序的，失败和成功的交叉去写 
2.1 判断：如果成功了，那就先退出，判断是否退出成功，退出成功，再继续参数化  
前提条件 类级别的装置函数(setup_class,teardown_class)
2.2 前提条件：装置函数可以用方法级别

'''
class TestLogin:
    def setup_class(self):
        '''
        初始化chrome对象
        :return:
        '''
        # 创建driver对象
        self.driver = Driver.get_drvier()
        # 创建login的业务对象
        self.login = Login(self.driver)
        # 创建base对象，调用page_source的方法
        self.base = Base(self.driver)

    @pytest.mark.parametrize('args',data)
    def test_login(self,args):
        self.login.login_business(args['accounts'],args['pwd'])
        time.sleep(2)
        assert args['assert'] in self.base.base_page_source


    def teardown_class(self):
        '''
        所有测试用例执行完毕关闭浏览器
        :return:
        '''
        Driver.close_driver()





