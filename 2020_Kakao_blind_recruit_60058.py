# 220904
# 2020 KAKAO BLIND RECRUITMENT > 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3

# 올바른 괄호 문자열인지 체크하는 함수
def isCorrect(s):
    correct = 0
    for j in range(len(s)):
        if s[j] == '(':
            correct += 1
        elif s[j] == ')':
            correct -= 1

        if correct < 0:     # ) 가 ( 보다 먼저 나오면 올바른 괄호 문자열이 아니므로
            return False
    return True

def solution(p):
    answer = ''

    if len(p) == 0 or isCorrect(p): return p

    # 균형잡힌 괄호 문자열인지 체크하는 부분
    left, right, i = 0, 0, -1
    while i == -1 or left != right:
        i += 1
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1
    u, v = p[:i+1], p[i+1:]

    if isCorrect(u):
        # u가 올바른 괄호 문자열일 때
        answer += u + solution(v)
    else:
        # u가 올바른 괄호 문자열이 아닐 때
        answer += '(' + solution(v) + ')'
        for c in u[1:-1]:
            if c == '(': answer += ')'
            else: answer += '('

        # 나의 오답 => 나머지 문자열의 "괄호 방향"을 뒤집어야 했음. 순서를 뒤집는게 아니라.
        # return '(' + solution(v) + ')' + u[1:-1][::-1]

    return answer
