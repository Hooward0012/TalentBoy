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
# print('大家好，我叫%s,今年 %d 岁！'%('howard', 18))
# print('大家好，我叫{0}, 我今年{1}岁 ！'.format('howard', 18))
# print('大家好，我叫{name}, 我今年{age}!'.format(name='howard', age = 18))
# name = 'howard'
# age = 18
# print(f'大家伙，我叫{name}, 今年{age}岁')

'''
字符分割
'''

# str1 = "2019-10-1 14:00:23"
# list = []
# list = str1.split(' ')
# print(list)
# list2 = str1.split(' ')[0].split('-')
# print(list2)
# list3 = str1.split(' ')[1].split(':')
# print(list3)
#

'''
String 的空格 和 大小写
'''
# str1 = '      beautiful world    '
# print(str1)
# str2 = str1.strip()
# print(str2)
#
# string = "ITS MOST BEAUTIFUL TIME OF YEAR"
# string2 = string.lower()
# print(string2)
# string3 = string2.upper()
# print(string3)

'''
String 的判断
'''
str1 = 'steph curry is my favourite player'
a = str1.startswith('steph')
print(a)
b = str1.endswith('player')
print(b)

