# 231119
# [PGS] 더 크게 합치기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181939

def solution(a, b):
    # 풀이 1
    # 형변환 사용
    '''
    a, b = str(a), str(b)
    return max(int(a+b), int(b+a))
    '''
    
    # 풀이 2
    # f-string 사용
    return max(int(f'{a}{b}'), int(f'{b}{a}'))
