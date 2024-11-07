# try:
#     x = 1/0
# except ZeroDivisionError as err:
#     print(f'程序发生异常，错误信息：{err}')
# except IndexError as err:
#     print(f'程序发生IndexError 异常， 错误信息：{err}')

try:
    x = 1/0
except (IndexError, ZeroDivisionError, IndexError) as err:
    print(f'程序发生异常，错误信息{err}')
finally:
    print('一定会被执行到的finally')
