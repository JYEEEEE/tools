class PeopleBody:
    pass


class PeopleTest():
    pass


# --->

class People(object):
    """
    注释
    """

    sex = None
    name = None
    age = None

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, x, y):
        # People 定义
        # self == 将来实例的对象
        # __init__ 用来初始化成员属性

        # 属性
        self.sex = None
        self.name = x
        self.age = y

    def p1(self):
        print(1)

    def __say_name(self):
        print(self.name)
        self.p1()

    def __say_age(self):
        print(self.age)

    def say_my_info(self):
        self.p1()
        self.__say_age()

    @classmethod
    def say_somethings(cls, words):
        # 不需要实例化，
        print(words)


r = People()
r.say_my_info()


r1 = People()
r2 = People()
r3 = People()


r1 = r2 = r3
