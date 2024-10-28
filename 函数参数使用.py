# def get_sum(a,b):
#     sum = a + b
#     return sum
#
# print(get_sum(3,5))

# def chang_list(list):
#     list[1] = 'fxxk'
#
# my_list = [1,2,3,4]
# chang_list(my_list)
# print(my_list)

# def add(a,b,/):
#     只想要按照顺序传递参数
#     print(a+b)
#
# add(1, 2)

# def add(*, a, b):
#     #只能按照 key-value 形式，不允许按顺序传递参数
#     print(a + b)
#
# add(a = 1, b = 2)
#
# def print_some(length, *age):
#     #一般就是在参数名称的前面添加 * 号，表示这个位置的参数可以是多个，比如这里我们定义可以传入多个 age
#     print('年龄:', *age)
#     print(age)
#     #我们传入的多个参数，被转化成元组了
#     print('长度', length)
#
# print_some(18,2,3,4,5,6,7,)

# def print_some(length, **age):
#     #两颗 * 的，它和一颗 * 不同之处就在于它会将传过来的多个参数转化成字典
#     print('年龄', age)
#     print('长度', length)
#
# print_some(length= 18, age = 3, age1 = 4, age2 = 5, age4 = 6)
# #所以调用的时候就需要用 key-value 的形式


def add(a,b):
    print(a+b)

l = [1,2]
#你调用函数的时候，参数在列表或元组或字典中，你可以使用 * 或 ** 来解包传递参数
add(*l)

d = {'a':1, 'b':2}
#如果是字典,用两个 * 号解包
add(**d)


