'''
常规实例方法
'''
# class Zoo:
#
#     def __init__(self, animals):
#         self.animals = animals
#
#
#     def get_animals(self):
#         return self.animals
#
#
# z = Zoo(['pig', 'Dog', 'Cat'])
# print(z.get_animals())


'''
类方法
'''
# class Zoo:
#
#     animals = ['Pig', 'Dog', 'Cat', 'Python']
#     def __init__(self, animals):
#         self.animals = animals
#
#     @classmethod
#     def get_animals(cls):
#         return cls.animals

# print(Zoo.get_animals())


'''
静态方法
静态方法不需要实例或类的引用，所以你可以通过实例访问静态方法也可以通过类来访问静态方法
'''


class Zoo:
    animals = ['pig', 'Dog', 'Cat']

    def __init__(self, animals):
        self.animals = animals

    @staticmethod
    def get_animals():
        return '这是静态方法的调用'


print(Zoo.get_animals())
z = Zoo(['panda', 'owl'])
print(z.get_animals())
