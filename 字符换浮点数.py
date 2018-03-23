# -*- coding: utf-8 -*-
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

from functools import reduce
def str2float(s):
    def char2num(s):
        return DIGITS[s]
    s=s.split('.')
    return reduce(lambda x,y:x*10+y,map(char2num,s[0]))+reduce(lambda x,y:x*0.1+y,map(char2num,s[1][::-1]))*0.1
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
