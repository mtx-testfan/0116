
from base.oepnDriver import OpenDriver

'''
单例模式:设计思想
类可以创建多少个对象  一个类可以创建很多对象
单例  类只能创建具有相同内存地址的对象  一个：所有创建的对象的内存地址都是一个 id(对象1) == id(对象2)
内存地址是一个
应用场景：回收站，任务管理器，日志，数据库连接池 单例模式
'''
import pageObject
class Driver:
    # 标记，用它来判断是否实例化过对象
    # 初始化，定义一下这个driver从来没有实例化过
    # 类属性 类方法是操作类属性的
    driver = None

    @classmethod
    def get_drvier(cls):
        ## 实例化driver对象  控制Chrome这个类只调用一次
        # 条件语句：判断一下driver属性是否被赋值过，即Chrome() 是否被实例化过
        if cls.driver is None:
            # 调用这个方法
            # cls.driver = webdriver.Chrome()  # 核心
            cls.driver = OpenDriver().get_driver('谷歌')  # 核心
            cls.driver.get(pageObject.url)
            cls.driver.maximize_window()
        return cls.driver
    @classmethod
    def close_driver(cls):
        # 为了程序的健壮性，需要判断下driver是否为None
        if cls.driver:
            cls.driver.quit()
            # 必须 置空的
            cls.driver = None   # 我们浏览器对象关闭了 没有了


if __name__ == '__main__':
    driver = Driver().get_drvier()
    print(id(driver))
    driver1 = Driver().get_drvier()
    print(id(driver1))
    Driver().close_driver()


