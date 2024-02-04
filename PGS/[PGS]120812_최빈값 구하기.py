# 240204
# [PGS] 최빈값 구하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120812


def solution(array):
    # 나의 풀이
    # 런타임 에러 발생
    '''
    if len(array) == 1:
        return array[0]

    d = {}
    for i in array:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1

    res = sorted(d.items(), key=lambda x: x[1], reverse=True)

    if res[0][1] == res[1][1]:
        return -1
    else:
        return res[0][0]
    '''

    # 풀이 1
    # list의 index와 count 활용
    '''
    count = [0] * (max(array)+1)

    for i in array:
        count[i] += 1

    max_cnt = max(count)
    f = 0
    for c in count:
        if c == max_cnt:
            f += 1

    if f > 1:
        return -1
    else:
        return count.index(max_cnt)
    '''

    # 풀이 2
    # Counter 객체의 most_common 메소드 활용
    from collections import Counter

    # 원본 array를 사용하면 런타임에러 발생
    # if len(array) == 1:
    #     return array[0]

    m = Counter(array).most_common(2)
    if len(m) == 1:
        return m[0][0]

    if m[0][1] == m[1][1]:
        return -1
    else:
        return m[0][0]



print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
