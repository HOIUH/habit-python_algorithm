# 231126
# [PGS] 숨어있는 숫자의 덧셈 (1) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    # 풀이 1
    # num_list와 for문 활용
    '''
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = 0
    for s in my_string:
        if s in num_list:
            answer += int(s)
    return answer
    '''

    # 풀이 2
    # isdigit
    return sum(int(s) for s in my_string if s.isdigit())

    # 풀이 3
    # re.sub
    '''
    import re
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))
    '''

    # 풀이 4
    # try except문
    '''
    answer = 0
    for s in my_string:
        try:
            answer += int(s)
        except:
            pass
    return answer
    '''


print(solution("aAb1B2cC34oOp"))
