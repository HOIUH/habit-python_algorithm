# 20220409
a, b = map(int, input().split())

if a < -10000 or a > 10000 or b < -10000 or b > 10000:
    print('입력값은 -10000 이상 10000 이하 정수값이어야 합니다.')
    a, b = map(int, input().split())

if a > b: print('>')
elif a < b: print('<')
elif a == b: print('==')
