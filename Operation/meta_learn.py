class PersonMeta(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print('---> PersonMeta.__init__')

    def __new__(cls, *args, **kwargs):
        print('---> PersonMeta.__new__')
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('---> PersonMeta.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj


class Person(metaclass=PersonMeta):

    def __init__(self, name, age):
        print('---> Person.__init__')
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('--->Person.__new__')
        return object.__new__(cls)


howard = Person('howard', 18)
