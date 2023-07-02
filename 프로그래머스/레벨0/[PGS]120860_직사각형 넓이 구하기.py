# 230702
# [PGS] 직사각형 넓이 구하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots):
    answer = 1
    a = dots.pop(0)

    for dot in dots:
        if dot[0] == a[0]:
            answer *= a[1] - dot[1]
        elif dot[1] == a[1]:
            answer *= a[0] - dot[0]

    return abs(answer)
