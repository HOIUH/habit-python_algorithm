# 221009
# 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

'''
1. from itertools import combinations => 조합 생성
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for menu_cnt in course:
        orders_combi = []
        # 메뉴 개수만큼 가능한 조합 생성
        for order in orders:
            orders_combi += combinations(sorted(order), menu_cnt)

    # 나의 풀이를 더 깔끔히 정리한 풀이
        orders_combi = Counter(orders_combi).most_common()
        answer += list(k for k, v in orders_combi if v > 1 and v == orders_combi[0][1])

    answer = [''.join(element) for element in answer]

    # 나의 풀이
    '''
        if orders_combi:
            max_cnt = orders_combi[0][1]
            if max_cnt < 2:
                continue

            for i in range(len(orders_combi)):
                element = orders_combi[i]
                if element[1] != max_cnt:
                    break
                else:
                    answer.append(''.join(element[0]))
    '''

    return sorted(answer)


# o, c = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
# o, c = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
o, c = ["XYZ", "XWY", "WXA"], [2, 3, 4]
print(solution(o, c))
