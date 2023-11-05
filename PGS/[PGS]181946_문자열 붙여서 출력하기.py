# 231105
# [PGS] 문자열 붙여서 출력하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181946

# 풀이 1
# split 사용
'''
str1, str2 = input().strip().split(' ')
print(str1 + str2)
'''

# 풀이 2
# replace 사용
print(input().strip().replace(' ', ''))
