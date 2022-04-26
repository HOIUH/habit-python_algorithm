# 20220426
# 상수
# https://www.acmicpc.net/problem/2908

#input_list = list(map(int, input().split()))
input_list = list(input().split())

# 파이썬스러운 방식
reverse1 = int(input_list[0][::-1])
reverse2 = int(input_list[1][::-1])

'''
# reversed() 사용하여 문자열 뒤집는 방법
str1 = reversed(input_list[0])
print(''.join(str1))
'''

if reverse1 > reverse2:
    print(reverse1)
else:
    print(reverse2)