# 230703
# [PGS] 배열 원소의 길이 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    answer = []

    for s in strlist:
        answer.append(len(s))

    return answer

    # 다른 사람 풀이
    # return [len(s) for s in strlist]
