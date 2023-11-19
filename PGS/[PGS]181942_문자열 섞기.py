# 231119
# [PGS] 문자열 섞기
# https://school.programmers.co.kr/learn/courses/30/lessons/181942

def solution(str1, str2):
    answer = ''
    
    # 풀이 1
    # for range 구문 사용
    '''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    '''
    
    # 풀이 2
    # zip 사용
    for s1, s2 in zip(str1, str2):
        answer += s1 + s2
    return answer
