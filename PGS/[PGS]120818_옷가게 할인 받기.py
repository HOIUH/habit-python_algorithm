# 240114
# [PGS] 옷가게 할인 받기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    # 풀이 1
    if price >= 500000:
        price *= 0.8
    elif price >= 300000:
        price *= 0.9
    elif price >= 100000:
        price *= 0.95

    return int(price)

    # 풀이 2
    # tuple 사용
    '''
    discounts = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0:1}
    for target_price, discount_rate in discounts.items():
        if price >= target_price:
            return int(price * discount_rate)
    '''
