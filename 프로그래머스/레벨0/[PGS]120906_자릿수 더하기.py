# 230827
# [PGS] 자릿수 더하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    # 나의 풀이
    '''
    answer = 0

    for e in str(n):
        answer += int(e)

    return answer
    '''

    # 다른 사람 풀이 1
    # sum() 함수와 map() 함수 사용
    # map(변환 함수, 순회 가능한 데이터)
    # return sum(map(int, str(n)))

    # 다른 사람 풀이 2
    # sum() 함수 사용
    return sum(int(e) for e in str(n))


print(solution(1234))
print(solution(930211))
