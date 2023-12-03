# 231203
# [PGS] 홀짝에 따라 다른 값 반환하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181935

def solution(n):
    # 풀이 1
    '''
    answer = 0

    if n % 2:  # 홀수
        for i in range(n + 1):
            if i % 2:  # 홀수
                answer += i
    else:  # 짝수
        for i in range(n + 1):
            if not (i % 2):  # 짝수
                answer += i * i

    return answer
    '''

    # 풀이 2
    # range의 step 옵션 활용
    '''
    if n % 2:  # 홀수
        # return sum(i for i in range(1, n+1, 2))
        return sum(range(1, n + 1, 2))
    # 짝수
    return sum(i * i for i in range(2, n + 1, 2))
    '''

    # 풀이 3
    n2 = n % 2
    return sum(i ** (2-(i%2)) for i in range(n+1) if n2 == i % 2)

