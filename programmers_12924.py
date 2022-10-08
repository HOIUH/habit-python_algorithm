# 221008
# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    # for문에선 n//2+1까지만 보고 n 자기자신은 마지막에 더해줌
    for i in range(1, n // 2 + 1):
        sum = 0
        x = i

        while sum < n:
            sum += x
            x += 1
        if sum == n:
            answer += 1

    return answer + 1


# 나의 풀이
# 복잡
'''
def continuous_plus(num: int, x: int) -> int:
    result = 0
    print(num, x)
    if x == (num - 1) / 2:
    # if num-x == x+1:
        result += 1
    # elif x <= (num - 1) / 2:
    elif num - x < x + 1 or num == x:
        result = 0
    else:
        result = continuous_plus(num - x, x + 1)
    print(f'result: {result}')
    return result


def solution(n):
    answer = 0
    for i in range(1, n // 2 + 1):
        answer += continuous_plus(n, i)
        print(f'answer: {answer}')

    return answer + 1
'''

print(solution(15))
