# 220517
# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

# 문제 풀이
# https://coding-grandpa.tistory.com/85
# Hash(해시) 설명
# https://yunaaaas.tistory.com/46

# Counter 사용한 풀이
# Python이 제공하는 collections라는 모듈의 한 class
# list를 가지고 Counter를 생성하면, Counter는 Key가 이름이고, Value가 count인 dictionary를 반환하게 된다.
import collections

def solution(participant, completion):
    # 1. participant의 Counter를 구한다
    # 2. completion의 Counter를 구한다
    # 3. 둘의 차를 구하면 정답만 남아있는 Counter를 반환한다
    answer = collections.Counter(participant) - collections.Counter(completion)
    # Counter class는 상호간의 뺄셈 연산을 지원한다

    # 4. Counter의 key값을 반환한다
    return list(answer.keys())[0]


    '''
    # Hash 사용한 풀이
    hashDict = {}
    sumHash = 0

    # 1. Hash: participant의 dictionary 만들기
    # 2. participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for c in completion:
        sumHash -= hash(c)

    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]
    '''

    '''
    # 효율성 테스트 FAIL
    for c in completion:
        participant.remove(c)

    answer = participant[0]
    return answer
    '''