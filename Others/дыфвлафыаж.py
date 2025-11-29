class SomeClass:

    def __init__(self, someattr1, someattr2):
        self.someattr1 = someattr1
        self.__someattr2 = someattr2

    def set_info(self, info):
        self.__someattr2 = info

    def get_info(self):
        return self.someattr1, self.__someattr2

obj1 = SomeClass(3, 123)
obj1.someattr1 = 2
obj1.set_info(14)
print(obj1.get_info())