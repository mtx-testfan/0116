import time

from pageAction.actions_manager import ActionsManager
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin
'''
第一种方法:在登录这个类中进行两个页面的实例化
第二种方法:多继承
'''
from base.driver import Driver

# # 第二种方法
# class Login(PageLogin,PageIndex):
#
#     # 组合业务：登录成功的业务
#     def login_success(self):
#         # 点击首页的登录链接
#         self.click_login_link()
#         # 输入用户名
#         self.input_username('yaoyao')
#         # 输入密码
#         self.input_pwd('yaoyao')
#         # 点击登录
#         self.click_login_button()
#
#     # 组合业务：登录的业务(参数化)
#     def login_business(self, username, password):
#         # 点击首页的登录链接
#         self.click_login_link()
#         # 输入用户名
#         self.input_username(username)
#         # 输入密码
#         self.input_pwd(password)
#         # 点击登录
#         self.click_login_button()

#第一种方法
class Login(ActionsManager):
    # 继承ActionsManager，做到了页面对象类实例化的最大复用性

    # 组合业务：登录成功的业务
    def login_success(self):
        # 点击首页的登录链接
        self.pageindex.click_login_link()
        # 输入用户名
        self.pagelogin.input_username('yaoyao')
        # 输入密码
        self.pagelogin.input_pwd('yaoyao')
        # 点击登录
        self.pagelogin.click_login_button()
        time.sleep(3)

    # 组合业务：登录的业务(参数化)
    def login_business(self,username,password):
        # 点击首页的登录链接
        self.pageindex.click_login_link()
        # 输入用户名
        self.pagelogin.input_username(username)
        # 输入密码
        self.pagelogin.input_pwd(password)
        # 点击登录
        self.pagelogin.click_login_button()
        time.sleep(3)


if __name__ == '__main__':
    driver = Driver.get_drvier()
    Login(driver).login_success()