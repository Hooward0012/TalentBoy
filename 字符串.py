'''
String 是不可变类型的，它是一种类似于列表的数据结构，
比如 “handsomeb” 这个字符串，你可以通过索引来访问字符串里面的字符
'''
# str = 'handsomeb'
# print(str[0])
# print(str[1])
# print(str[2])

'''
使用r来显示原始字符
'''
# str = '1234\n567'
# print(str)
# str1 = r'1234\n567'
# print(f'str1:{str1}')

'''
字符串拼接
'''
# str1 = 'fxxk'
# str2 = 'python'
#
# str1 += str2
# str1 = str1 + str2
#
# text = 'fxxk' 'python' '!!!'
# print(text)

'''
格式化
1、 %s ： 字符格式化

2、 %d : 整型格式化

3、 format方法

4、 f-string
'''
print('大家好，我叫%s,今年 %d 岁！'%('howard', 18))
print('大家好，我叫{0}, 我今年{1}岁 ！'.format('howard', 18))
print('大家好，我叫{name}, 我今年{age}!'.format(name='howard', age = 18))
name = 'howard'
age = 18
print(f'大家伙，我叫{name}, 今年{age}岁')
