import re

def convert_number(str: str):
    if str[0] == '+':
        str = '8' + str[2:]
    
    str = "".join(re.findall(r'\d', str, re.S))
    if len(str) == 7:
        return '8495' + str
    return str

num = convert_number(input())
for _ in range(3):
    if convert_number(input()) == num:
        print('YES')
    else:
        print('NO')

