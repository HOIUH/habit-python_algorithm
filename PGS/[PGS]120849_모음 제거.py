# 231126
# [PGS] 모음 제거 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):

    # 풀이 1
    # for문과 replace 활용
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel:
        my_string = my_string.replace(v, '')

    return my_string
    '''

    # 풀이 2
    # join()과 list comprehension 활용
    # return "".join([s for s in my_string if s not in 'aeiou'])

    # 풀이 3
    # re.sub 정규표현식 사용
    import re
    return re.sub('[aeiou]', '', my_string)
    # return re.sub(r"a|e|i|o|u", "", my_string)


print(solution("nice to meet you"))
