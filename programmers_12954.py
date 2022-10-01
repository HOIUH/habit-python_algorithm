# 221001
# x만큼 간격이 있는 n개의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):

    return [i * x + x for i in range(n)]

'''
    # 나의 풀이
    answer = []
    tmp = x

    while len(answer) < n:
        answer.append(tmp)
        tmp += x

    return answer
'''

print(solution(2, 5))