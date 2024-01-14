# 240114
# [PGS] 아이스 아메리카노 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120819

def solution(money):
    # 풀이 1
    # divmod 활용
    return list(divmod(money, 5500))    # divmod return type: 튜플

    # 풀이 2
    # return [money // 5500, money % 5500]



