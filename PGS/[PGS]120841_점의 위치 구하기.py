# 231231
# [PGS] 점의 위치 구하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    # 풀이 1
    '''
    x, y = dot
    if x > 0:  # 1, 4 사분면
        return 1 if y > 0 else 4
    else:  # 2, 3 사분면
        return 2 if y > 0 else 3
    '''

    # 풀이 2
    quad = [(3, 2), (4, 1)]
    return quad[dot[0] > 0][dot[1] > 0]
