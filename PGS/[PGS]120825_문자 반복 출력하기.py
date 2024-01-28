# 240128
# [PGS] 문자 반복 출력하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120825


def solution(my_string, n):
    # 풀이 1
    # for 문 사용
    '''
    answer = ''
    for s in my_string:
        answer += s * n
    return answer
    '''

    # 풀이 2
    # return ''.join(list(s*n for s in my_string))
    return ''.join(s*n for s in my_string)  # join 내부 return type: generator

