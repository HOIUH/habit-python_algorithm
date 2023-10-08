# 231008
# [PGS] 주식가격 / 레벨2
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    # 나의 풀이
    '''
    answer = []
    prices_length = len(prices)

    for i in range(prices_length):
        period = prices_length - 1 - i      # 끝까지 가격 떨어지지 않는 경우

        for j in range(i+1, prices_length):     # prices[i] 뒤 요소들 중
            if prices[j] < prices[i]:           # 가격 떨어지는 경우 있으면
                period = j-i                    # 해당 인덱스에서 i 뺀 값을 담고
                break                           # 루프 멈추기
        answer.append(period)

    return answer
    '''

    # 다른 사람 풀이
    # collections.deque 사용
    from collections import deque

    answer = []
    prices = deque(prices)

    while prices:
        x = prices.popleft()
        count = 0

        for e in prices:
            count += 1
            if x > e:
                break

        answer.append(count)

    return answer


print(solution([1, 2, 3, 2, 3]))
