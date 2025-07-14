"""
功能简述：类继承
1. 父类有构造函数，子类没有自己的构造函数，实例化时直接使用父类的构造函数，且可以直接使用父类的类方法。
2. 子类的构造函数中,需要调用父类的构造函数，使用super()函数。


@File           : class_inheritance.py
@Author         : Elson.L
@Created        : 2025-07-10
@Last Modified  : 2025-07-10
@Version        :
"""


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def achieve_name(self) -> str:
        return self.name


class Hitman(Human):
    def __init__(self, id: int, level: int, name: str, age: int):
        super(Hitman, self).__init__(name, age)  # 调用父类构造函数
        self.id = id
        self.level = level

    def blood_contract(self):
        print("Signed a new contract.")


class Target(Human):
    def __init__(self, id: int, level: int):
        self.id = id
        self.level = level


hitman_47 = Hitman(47, 10, "Unknow", 32)
print(hitman_47.achieve_name())
