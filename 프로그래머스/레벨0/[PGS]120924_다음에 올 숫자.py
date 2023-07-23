# 230723
# [PGS] 다음에 올 숫자 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):

    # 나의 풀이
    # x == 0 조건문 따로 뺄 필요 없음
    '''
    last = common[-1]
    llast = common[-2]
    x = last - llast

    if x == 0:
        answer = last
    elif x == (common[1] - common[0]):  # 등차수열
        answer = last + x
    else:                               # 등비수열
        answer = last * (last // llast)

    return answer
    '''

    # 다른 사람 풀이
    # common 리스트의 앞 3개 요소만 사용하여 등차, 등비 판별
    a, b, c = common[:3]

    if (b - a) == (c - b):              # 등차수열
        answer = common[-1] + (b - a)
    else:                               # 등비수열
        answer = common[-1] * (b // a)

    return answer


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
print(solution([2, 2, 2, 2]))
