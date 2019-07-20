"""
实现一个单例模式类的定义

多次实例化，得到都是相同的实例对象
"""


class MongoClient(object):
    """
    数据库单例客户端
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        step1: 定义一个变量，用于存储实例
        step2: 创建实例时，先判断变量是否为None，若None，则创建，并将该实例赋值给变量
               若not None，返回该变量

        :param args:
        :param kwargs:
        :return:
        """
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self._instance = '11111'


c1 = MongoClient()
c2 = MongoClient()

print(id(c1))
print(id(c2))
assert id(c1) == id(c2), 'c1 not equal c2.'
