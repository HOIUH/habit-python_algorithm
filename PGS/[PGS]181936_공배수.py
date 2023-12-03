# 231203
# [PGS] 공배수 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181936

def solution(number, n, m):
    # 오답
    # 반례) 18, 9, 3
    '''
    nm = n * m
    return int(number % nm == 0)
    '''

    # 풀이 1
    # == 연산의 결과는 bool 타입
    # bool 타입 결과를 int로 변환하여 리턴
    # & 활용
    return int((number % n == 0) & (number % m == 0))
