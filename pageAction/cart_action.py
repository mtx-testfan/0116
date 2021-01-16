import time

from pageAction.actions_manager import ActionsManager
from pageObject.page_index import PageIndex

'''
组合业务
引入页面对象包里面的步骤
继承
'''
class Cart(ActionsManager):
    # 组合业务:添加购物车
    def business_add_cart(self):
        self.pageindex.click_zk_skirt()
        self.pageindex.switch_window()
        self.pagegoodsdetail.click_pink()
        time.sleep(2)
        self.pagegoodsdetail.click_M()
        time.sleep(2)
        self.pagegoodsdetail.click_add_cart()

    # 组合业务:删除购物车
    def business_delete_cart(self):
        '''
        功能测试 手动如何操作 -----自动化动作就如何操作
        删除商品之前我们要确保购物车里面有商品
      (推荐)  1. action层，先调用添加购物车这个业务（确保购物车里面有商品），再调用删除业务
      1.1 动作能关联上
        2. case层，调整顺序，插件pytest-ordering (不推荐：测试用例和测试用例之间是相互独立，不依赖)
        :return:
        '''
        # 调用添加业务
        self.business_add_cart()
        # 调用删除业务
        self.pagegoodsdetail.click_right_cart()
        self.pagecart.click_delete_button()
        self.pagecart.click_confirm_delete()
    #点击首页
    def click_index(self):
        pass

if __name__ == '__main__':
    pass