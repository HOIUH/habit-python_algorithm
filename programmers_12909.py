# 221017
# 스택/큐 > 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    # 풀이 1. 숫자 이용
    stack = 0
    for element in s:
        if element == '(':
            stack += 1
        else:
            if stack == 0:
                return False
            else:
                stack -= 1

    return False if stack else True

# 풀이 2. List로 Stack 구현
'''
    stack = []
    for element in s:
        if element == '(':
            stack.append(element)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True
'''

# print(solution("(())()"))
print(solution("(()("))
