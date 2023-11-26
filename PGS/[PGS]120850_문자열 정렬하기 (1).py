# 231126
# [PGS] 문자열 정렬하기 (1) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    # 풀이 1
    # num_list와 for문 활용
    '''
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    answer = []
    for s in my_string:
        if s in num_list:
            answer.append(int(s))
    return sorted(answer)
    '''

    # 풀이 2
    # try except문 활용
    '''
    answer = []
    for s in my_string:
        try:
            answer.append(int(s))
        except:
            pass
    return sorted(answer)
    '''

    # 풀이 3
    # isdigit()과 list comprehension 활용
    return sorted([int(s) for s in my_string if s.isdigit()])


print(solution("hi12392"))
