# 230820
# [PGS] 숫자 찾기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):

    i = str(num).find(str(k))

    # 나의 풀이
    '''
    if i + 1:
        return i + 1
    else:
        return -1
    '''

    return i + 1 if i >= 0 else i


print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))
