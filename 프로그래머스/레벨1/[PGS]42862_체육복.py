# 230619
# [PGS] 체육복 / 레벨1
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# lost, reserve 둘다에 속해 있는 요소를 먼저 제거해야해서 차집합 활용
def solution(n, lost, reserve):
    answer = n
    reserve, lost = set(reserve), set(lost)
    new_lost = lost - reserve
    new_reserve = reserve - lost

    for e in new_lost:
        if e-1 in new_reserve:
            new_reserve.remove(e-1)
        elif e+1 in new_reserve:
            new_reserve.remove(e+1)
        else:
            answer -= 1

    return answer
