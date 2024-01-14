# 240114
# [PGS] 외계행성의 나이 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    # 풀이 1
    alphabet, answer = 'abcdefghij', ''
    age = str(age)
    for e in age:
        answer += alphabet[int(e)]

    return answer

