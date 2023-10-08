# 231008
# [PGS] 완주하지 못한 선수 / 레벨2
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # 나의 풀이
    '''
    from collections import Counter

    p = Counter(participant)
    c = Counter(completion)

    for k in p.keys():
        if p[k] != c[k]:
            return k
    '''

    # 다른 사람 풀이
    # Counter class는 상호간의 뺄셈 연산 지원
    from collections import Counter

    # 1. participant의 Counter를, completion의 Counter를 구한다
    # 2. 둘의 차를 구하면 정답만 남아있는 Counter를 반환
    answer = Counter(participant) - Counter(completion)

    # 3. Counter의 key값을 반환한다
    return list(answer.keys())[0]
    # return answer.keys() => 결과: dict_keys(['leo']) 이런식으로 나와서 list 변환 필요


# 효율성 테스트 실패
'''
    while completion:
        p = participant.pop()

        try:
            completion.pop(completion.index(p))
        except ValueError:
            return p

    return participant[0]
    '''


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))