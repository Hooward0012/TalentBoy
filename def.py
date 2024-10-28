age = 18

def my_func():
    name = 'howard'
    print(name)

    global age = age + 1
    print(age)

my_func()