# 230616
# [PGS] 평행 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

# 직선 평행하기 위한 조건
# 1. 직선의 기울기(=y증가량/x증가량)가 같아야 함
# 2. y절편(=y축과 만나는 점. x=0)은 달라야 함

# 직선의 기울기 구하는 함수
def slope(d1, d2):
    return (d1[1] - d2[1]) / (d1[0] - d2[0])


def solution(dots):
    answer = 0
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]

    if slope(a, b) == slope(c, d):
        answer = 1
    if slope(a, c) == slope(b, d):
        answer = 1
    if slope(a, d) == slope(b, c):
        answer = 1

    return answer
