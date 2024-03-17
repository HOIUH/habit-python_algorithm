# 240317
# [PGS] 추억 점수 / 레벨1
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []

    for p in photo:
        tmp = 0
        for e in p:
            if e in name:
                tmp += yearning[name.index(e)]
        answer.append(tmp)

    return answer

