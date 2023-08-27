# 230827
# [PGS] OX퀴즈 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    # 나의 풀이
    '''
    answer = []
    for e in quiz:
        e_split = e.split()

        if e_split[1] == '-':
            correct = int(e_split[0]) - int(e_split[2])
            if correct == int(e_split[-1]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            correct = int(e_split[0]) + int(e_split[2])
            if correct == int(e_split[-1]):
                answer.append('O')
            else:
                answer.append('X')
    return answer
    '''

    # 다른 사람 풀이 1
    # 나의 풀이를 보다 깔끔하게 정리
    answer = []
    for e in quiz:
        a, op, b, eq, c = e.split()

        if op == '-':
            res = 'O' if int(c) == int(a) - int(b) else 'X'
            answer.append(res)
        elif op == '+':
            res = 'O' if int(c) == int(a) + int(b) else 'X'
            answer.append(res)

    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))

# 다른 사람 풀이 2 (참고만)
# eval() 함수 사용한 풀이
# => 보안때문에 eval()은 실제로 거의 사용하지 않음! 사용자가 프로그램 조종 가능
'''
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(quiz):
    return ['O' if valid(q) else 'X' for q in quiz]
'''