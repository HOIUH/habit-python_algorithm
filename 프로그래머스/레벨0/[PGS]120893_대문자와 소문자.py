# 231003
# [PGS] 대문자와 소문자 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    # 나의 풀이
    '''
    answer = ''
    for ch in my_string:
        if ch.islower():
            answer += ch.upper()
        else:
            answer += ch.lower()
    return answer
    '''

    # 다른 사람 풀이 1
    # swapcase() => 대소문자 상호변환
    # return my_string.swapcase()

    # 다른 사람 풀이 2
    # list comprehension => if else for 순서 지키기!
    # [조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data]
    return ''.join([ch.upper() if ch.islower() else ch.lower() for ch in my_string])


print(solution('cccCCC'))
