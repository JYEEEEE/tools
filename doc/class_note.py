class People(object):
    """
    类： 属性和方法的集合
    类名通常要求首字母大写
    """
    def __new__(cls, *args, **kwargs):
        """
        相当于构造函数，类被实例化的初始步骤
        """

        print('create A done.')
        return object.__new__(cls)

    def __init__(self, name, *args, **kwargs):
        """
        初始化函数
        """
        self.name = name
        print('init A done.')

    def _say(self, words):
        """
        函数名前的单引号 _ 表示该方法是个(protected)受保护方法，
        __ 开头的是私有方法。 首尾都有 __ 的是内置方法。
        讲道理不能被调用，但是python不限制。如果调用了，就会
        提示一个警告信息。

        类似的参考java或C：
        protect == _
        private == __
        public == 不加限制
        """
        print('%s say: %s' % (self.name, words))

    def say(self, words: str = 'hello'):
        """
        为了防止函数被修改，通常用 _ 开头的保护方法或 __ 开头的
        私有方法实现具体逻辑，再用不加限制的成员方法开放入口。
        参数里含self的为成员函数，self是成员函数默认传入的参数。
        """
        self._say(words)

    @classmethod
    def print_me(cls, words):
        """
        @classmethod是一个装饰器，在此处标识这个函数为类方法，
        意思为不需要实例化就可以调用的方法。
        类方法默认会将自身作为参数传入。
        """

        print(words)


# 测试代码
if __name__ == '__main__':
    print(People.print_me.__doc__)  # 打印该函数的注释信息
    People.print_me('人类的本质是复读机。')
    print('----------------------------')

    jyeeee = People('jyeeee')
    jyeeee.say('李佳星你能不能不要气我了(╯▔皿▔)╯')
    print('----------------------------')

    jyeeee.print_me('tips： 已经实例化对象也能够调用类方法。但是不建议。')


# 总结
# People：是实例
# jyeeee是实例化的对象
# 所以呢，类是比较虚的概念，实例化的对象是具体的事物。
# 比如水果是概念， 苹果是实例对象， 爷爷辈是概念， 爷爷是实例对象

# ---output ---
"""
        @classmethod是一个装饰器，在此处标识这个函数为类方法，
        意思为不需要实例化就可以调用的方法。
        类方法默认会将自身作为参数传入。

人类的本质是复读机。
----------------------------
create A done.
init A done.
jyeeee say: 李佳星你能不能不要气我了(╯▔皿▔)╯
----------------------------
tips： 已经实例化对象也能够调用类方法。"""