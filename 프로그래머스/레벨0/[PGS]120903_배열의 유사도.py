# 230820
# [PGS] 배열의 유사도 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):

    # 나의 풀이
    '''
    answer = 0

    for element in s1:
        if element in s2:
            answer += 1

    return answer
    '''

    # 다른 사람 풀이
    # set 자료구조와 교집합 활용
    return len(set(s1) & set(s2))


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))
