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

def add(*, a, b):
    #只能按照 key-value 形式，不允许按顺序传递参数
    print(a + b)

add(a = 1, b = 2)