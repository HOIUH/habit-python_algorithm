# 230723
# [PGS] 문자열 밀기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    # 나의 풀이
    '''
    answer = 0

    if A == B:
        return answer

    for i in range(len(A) - 1, -1, -1):
        answer += 1
        tmp = A[i:] + A[:i]
        if tmp == B:
            return answer

    return -1
    '''

    # 다른 사람 풀이
    # find 함수 이용한 풀이
    # find(찾을문자) => 찾는 문자 1. 존재하면 해당 위치의 index 반환
    #                          2. 존재하지않으면 -1 반환
    #                          3. 여러개 존재하면 맨 처음 index 반환
    return (B * 2).find(A)


print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("abc", "abc"))
