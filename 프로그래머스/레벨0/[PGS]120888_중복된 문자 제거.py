# 230709
# [PGS] 중복된 문자 제거 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = ''

    for s in my_string:
        if s not in answer:
            answer += s

    return answer
