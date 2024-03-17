# 240317
# [PGS] 수 조작하기 1 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    w = control.count('w') * 1
    s = control.count('s') * (-1)
    d = control.count('d') * 10
    a = control.count('a') * (-10)
    return n+w+s+d+a

