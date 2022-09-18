# 220918
# 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

'''
1. deque 생성 시 maxlen 지정하면 deque 사이즈 고정됨.
나중에 들어온 데이터들이 저장됨.
collections.deque(['a', 'b', 'c', 'd'], maxlen=3)
=> 결과: deque(['b', 'c', 'd'], maxlen=3)
'''

from collections import deque

def solution(cacheSize, cities):
    # deque의 maxlen을 사용한 풀이
    # cache miss 발생해도 cache.popleft() 할 필요 없음
    answer = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)

    return answer

# cacheSize 0인 경우를 별도 if문으로 뺀 풀이
'''
    if cacheSize == 0: 
        return 5 * len(cities)
    
    answer = 0
    cache = deque([''] * cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
            cache.popleft()
        cache.append(city)

    return answer
'''

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities))