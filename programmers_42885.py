# 221027
# 탐욕법(Greedy) > 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        if len(people) == 1:
            answer += 1
            break
        elif people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            people.pop()
        else:
            answer += 1
            people.pop()

    return answer

print(solution([70, 50, 80, 50], 100))