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
str1 = 'fxxk'
str2 = 'python'

str1 += str2
str1 = str1 + str2
print(str1)