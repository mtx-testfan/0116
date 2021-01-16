import time

from pageAction.actions_manager import ActionsManager
from pageObject.page_index import PageIndex

'''
组合业务
引入页面对象包里面的步骤
继承
'''
class Order(ActionsManager):
    # 组合业务:提交订单，并提示提交成功(断言)
    def business_order(self):
        self.pageindex.click_zk_skirt()
        self.pageindex.switch_window()
        self.pagegoodsdetail.click_pink()
        time.sleep(1)
        self.pagegoodsdetail.click_M()
        time.sleep(1)
        self.pagegoodsdetail.click_now_buy()
        self.pagebuy.click_payment()
        self.pagebuy.click_submit_order()


if __name__ == '__main__':
    pass