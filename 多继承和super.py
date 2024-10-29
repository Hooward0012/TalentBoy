# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
#     def eat(self, food):
#         print(f'{self.name} eats {food}')
#
#
# class YellowPeople(Person):
#
#     def __init__(self, name, age, weight):
#         Person.__init__(self,name, age)#可以直接使用 super 类的名称进行调用，比如这样：
#         self.weight = weight
#
#     def print_some(self):
#         print(f'{self.name}, 今年{self.age}, 体重{self.weight}')
#
#
# howard = YellowPeople('howard', 18, 140)
# howard.print_some()
#
#

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self,food):
        print(f'{self.name} eats {food}')

class YellowPeopleFather(Person):
    def eat(self, food):
        print(f'{self.name}, 调用的是YellowPeopleFather的{food}')

class WhitePersonMother(Person):
    def eat(self, food):
        print(f'{self.name}, 调用的是WhitePersonMother的{food}')

class Son(YellowPeopleFather, WhitePersonMother):
    def eat(self, food):
        super(YellowPeopleFather, self).eat(food)

howard = Son('howard', 18)
howard.eat('banana')
print(Son.__mro__)
