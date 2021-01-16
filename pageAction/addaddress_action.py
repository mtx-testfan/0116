from pageAction.actions_manager import ActionsManager


class AddAddress(ActionsManager):
    # 组合业务
    def addaddress_business(self):
        self.pageindex.click_person_center()
        self.pagepersoncenter.click_my_address()
        self.pagemyaddress.click_new_address()
        # 切换iframe
        self.pagemyaddress.switch_to_iframe()
        self.pagemyaddress.input_name()
        self.pagemyaddress.input_tel()
        self.pagemyaddress.select_prov()
        self.pagemyaddress.select_city()
        self.pagemyaddress.select_country()
        self.pagemyaddress.input_detail_address()
        self.pagemyaddress.address_nickname()
        self.pagemyaddress.address_save()



