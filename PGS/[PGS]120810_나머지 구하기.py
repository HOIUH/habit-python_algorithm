# 240218
# [PGS] 나머지 구하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120810

def solution(num1, num2):
    # 풀이 1
    # return num1%num2
    
    # 풀이 2
    # 나눗셈을 뺄셈으로 구현
    while num1 >= num2:
        num1 -= num2
    return num1
