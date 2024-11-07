'''
创建一个闭包,它得是一个嵌套函数，接着内部函数引用 nonlocal 变量，最后嵌套函数的返回是内部函数
'''
def outer_fun(x):
    def inner_fun(y):
        print(x + y)
    return inner_fun

outer = outer_fun(5)
outer(1)
outer(2)
outer(3)
