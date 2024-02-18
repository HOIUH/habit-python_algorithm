# 240218
# [PGS] 문자열 뒤집기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120822

def solution(my_string):
    # 풀이 1
    # [시작:끝:방향]
    return my_string[::-1]

    # 풀이 2
    # return ''.join(list(reversed(my_string)))   # reversed() return type: class reversed


print(solution("jaron"))
