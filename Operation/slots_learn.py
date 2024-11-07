'''
快速访问类的属性
'''
# import timeit
#
#
# class Person:
#     def __init__(self):
#         self.name = 'howard'
#         self.age = 18
#
#
# howard = Person()
# print(howard.name)
#
#
# def test_fn(obj):
#     def set_del_attr():
#         obj.name = 'howard'
#         obj.name
#         del obj.name
#
#     return set_del_attr
#
#
# #
# print(min(timeit.repeat(test_fn(howard), number=1000000)))

'''
限制类的实例属性
'''
# class Person:
#     __slots__ = ['name', 'age', 'sex']
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# howard = Person('howard', 18, 'male')
# print(howard.name)
# print(howard.age)
# print(howard.sex)
#
# howard.plan = 'hard work'
# print(howard.plan)

'''
优化内存
'''

from memory_profiler import profile


# class Person:
#     __slots__ = ['name', 'age', 'sex']
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# @profile()
# def test_mem():
#     list([Person('howard', 18, 'male') for i in range(10000)])
#
#
# if __name__ == '__main__':
#     test_mem()
