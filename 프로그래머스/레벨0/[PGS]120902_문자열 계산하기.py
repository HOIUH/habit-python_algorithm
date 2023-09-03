# 230903
# [PGS] 문자열 계산하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120902

def solution(my_string):
    # 연산자가 여러개일 수 있음

    # 나의 풀이
    # eval 함수는 보안 취약하므로 사용 지양!
    # return eval(my_string)

    # 다른 사람 풀이 1
    '''
    s = my_string.split()
    answer = int(s[0])

    for i in range(1, len(s), 2):
        if s[i] == '+':
            answer += int(s[i+1])
        else:
            answer -= int(s[i+1])

    return answer
    '''

    # 다른 사람 풀이 2
    # 뺄셈을 덧셈과 음수로 변경한 뒤, 덧셈 기준 split
    x = my_string.replace('- ', '+ -').split(' + ')
    return sum(map(int, x))


print(solution('3 + 4 - 2'))
