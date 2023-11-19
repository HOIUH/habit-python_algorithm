# 231119
# [PGS] 두 수의 연산값 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181938

def solution(a, b):
    return max(int(f'{a}{b}'), 2*a*b)
