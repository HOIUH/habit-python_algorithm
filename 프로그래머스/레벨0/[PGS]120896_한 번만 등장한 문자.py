# 230910
# [PGS] 한 번만 등장한 문자 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    # 나의 풀이
    '''
    answer = ''

    s = ''.join(sorted(s))
    while s:
        if s[0] not in s[1:]:
            answer += s[0]
        s = s.replace(s[0], '')

    return answer
    '''

    # 다른 사람 풀이 1
    # count() 함수 사용
    return ''.join(sorted([ch for ch in set(s) if s.count(ch) == 1]))

    # 다른 사람 풀이 2
    # collections.Counter 객체 사용
'''
    from collections import Counter
    counter = Counter(s)
    unique_alphabets = filter(lambda alphabet: counter[alphabet] == 1, counter.keys())
    return ''.join(sorted(unique_alphabets))
    '''


ss = ["abcabcadc", "abdc", "hello"]
print(solution(ss[0]))
print(solution(ss[1]))
print(solution(ss[2]))
