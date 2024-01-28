# 240128
# [PGS] 각도기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120829


def solution(angle):
    '''
    90으로 나누면
    예각: 0.xx = > 1
    직각: 1.0 = > 2
    둔각: 1.xx = > 3
    평각: 2.0 = > 4
    '''

    s, r = divmod(angle, 90)
    if s == 0:
        return 1
    elif s == 2:
        return 4
    else:
        if r == 0:
            return 2
        return 3

    # 다른 풀이
    # return (angle // 90) * 2 + (angle % 90 > 0) * 1
