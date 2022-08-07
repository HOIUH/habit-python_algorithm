# 220807
# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# 참고: https://sohee-dev.tistory.com/123
# 내 노션 정리: https://www.notion.so/f9e057b63e134c3689b44c280e668b18

'''
1. Binary Search (이진 탐색) => 이분 탐색의 범위와 기준을 어떻게 잡을지가 핵심!
'''

def solution(n, times):
    answer = 0

    # right 은 가장 비효율적으로 심사했을 때 걸리는 시간.
    # 가장 긴 심사시간이 소요되는 심사관에게 n명 모두 심사받는 경우.
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 for문을 나간다.
            if people >= n:
                break

        # 심사한 사람의 수(people)가 심사 받아야 할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수(people)가 심사 받아야 할 사람의 수(n)보다 적은 경우
        else:
            left = mid + 1

    return answer