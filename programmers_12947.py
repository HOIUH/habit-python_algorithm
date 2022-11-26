# 221126
# 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    # 나의 풀이 좀 더 간단하게
    # return True if x % sum(int(e) for e in str(x)) == 0 else False
    return x % sum(int(e) for e in str(x)) == 0

'''
    # 나의 풀이
    answer = False
    x_str, divisor = str(x), 0

    for element in x_str:
        divisor += int(element)

    if x % divisor == 0:
        answer = True

    return answer
'''

print(solution(10))
