# def division(a, b):
#     assert b != 0, "除数不能为0"
#     return a / b
#
#
# division(5, 0)

def get_list_size(arg):
    assert isinstance(arg, list), "传入的参数必须是list类型"
    return len(arg)


get_list_size('fxxk python')
