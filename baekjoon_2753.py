# 20220411
# 윤년 구하기
# https://www.acmicpc.net/problem/2753

year = int(input())

if (year % 400) == 0:
    print('1')
elif (year % 100) == 0:
    print('0')
elif (year % 4) == 0:
    print('1')
else:
    print('0')

'''
if (year % 4) == 0:
    if (year % 400) == 0:
        print('1')
    elif (year % 100) == 0:
        print('0')
else: print('0')
'''
