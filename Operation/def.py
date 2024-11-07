# age = 18
#
# def my_func():
#     name = 'howard'
#     print(name)
#
#     global age
#     age = age + 1
#     print(age)
#
# my_func()

# age = 18
#
# def my_func():
#     age = 66
#     def my_inner_func():
#         nonlocal  age
#         age += 1
#         print(age)
#     my_inner_func()
#
# my_func()

age = 18

def my_func():
    age = 66
    def my_inner_func():
        global  age
        age += 1
        print(age)
    my_inner_func()

my_func()