import copy

'''
对于不可变的对象like：int,string,Tuple，复制时是开辟新的空间,把name绑定到
对象去
对于可变的对象like：List, dict,set，复制时在原有空间续写，往往可以利用他们
的内置方法对对象本身进行copy
'''
class Person:
    def __init__(self, name, age, lists):
        self.name = name
        self.age = age
        self.lists = lists

    def eat(self):
        print(self.name, '正在吃')

    def get_list(self):
        print(self.lists)

'''
浅拷贝得到的list_b并非完全独立，只是开辟了新的空间，但引用还是原来值
'''
# howard = Person('howard', 18, [1, 2, 3])
# p = copy.copy(howard)
# howard.name = 'MAGA'
# howard.lists[0] = 1105
# howard.eat()
# howard.get_list()
#
# p.eat()
# p.get_list()


'''
深拷贝是构建完完全全的新的对象，遍历递归原有的对象，然后深层次的复制，和原有的对象没有一点
关系
'''
howard = Person('howard', 18, [1,2,3])
p = copy.deepcopy(howard)

howard.name = 'MAGA'
howard.lists[0] = 1234
howard.eat()
howard.get_list()

p.eat()
p.get_list()

print(p is howard)
